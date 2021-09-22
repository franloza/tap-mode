"""REST client handling, including ModeStream base class."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Iterable

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream
from tap_mode.auth import ModeAuthenticator


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ModeStream(RESTStream):
    """Mode stream class."""

    _url_base = "https://app.mode.com/api/"

    records_jsonpath = "$[*]"

    @property
    def authenticator(self) -> ModeAuthenticator:
        """Return a new authenticator object."""
        return ModeAuthenticator.create_for_stream(self,
                                                   username=self.config.get('auth_token'),
                                                   password=self.config.get('password')
                                                   )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        next_page_token = None
        if response.json()['_embedded'][self.tap_stream_id]:
            next_page_token = previous_token + 1 if previous_token else 2
        return next_page_token

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {"page": next_page_token if next_page_token else 1}
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    @property
    def url_base(self) -> str:
        return self._url_base + self.config.get('workspace')

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from extract_jsonpath(self.records_jsonpath, input=response.json())


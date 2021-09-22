"""Mode tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th

from tap_mode.streams import (
    ReportsStream, SpacesStream
)

STREAM_TYPES = [
    ReportsStream,
    SpacesStream
]


class TapMode(Tap):
    """Mode tap class."""
    name = "tap-mode"

    config_jsonschema = th.PropertiesList(
        th.Property("auth_token", th.StringType, required=True),
        th.Property("password", th.StringType, required=True),
        th.Property("workspace", th.StringType, required=True),
        th.Property("user_agent", th.StringType, default="Tap-Mode"),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

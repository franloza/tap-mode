"""Stream type classes for tap-mode."""

from pathlib import Path
from typing import Optional

from tap_mode.client import ModeStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class SpacesStream(ModeStream):
    """Define sites stream."""
    name = "spaces"
    path = "/spaces"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "spaces.json"
    records_jsonpath = "$._embedded.spaces[*]"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {
            "space_token": record["token"]
        }


class ReportsStream(ModeStream):
    """Define reports stream."""
    parent_stream_type = SpacesStream
    name = "reports"
    path = "/spaces/{space_token}/reports"
    primary_keys = ["id"]
    replication_key = None
    schema_filepath = SCHEMAS_DIR / "reports.json"
    records_jsonpath = "$._embedded.reports[*]"

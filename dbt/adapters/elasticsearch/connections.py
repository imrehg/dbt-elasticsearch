from dataclasses import dataclass
from typing import Optional

from dbt.adapters.base import Credentials
from dbt.adapters.sql import SQLConnectionManager


@dataclass
class ElasticsearchCredentials(Credentials):
    host: str
    port: int = 9200
    api_key_id: Optional[str] = None
    api_key_secret: Optional[str] = None

    @property
    def type(self):
        return "elasticsearch"

    def _connection_keys(self):
        """
        List of keys to display in the `dbt debug` output.
        """
        # Omit fields like 'password'!
        return ("host", "port", "api_key_id")


class ElasticsearchConnectionManager(SQLConnectionManager):
    TYPE = "elasticsearch"

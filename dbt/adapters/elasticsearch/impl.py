from dbt.adapters.sql import SQLAdapter
from dbt.adapters.elasticsearch import ElasticsearchConnectionManager


class ElasticsearchAdapter(SQLAdapter):
    ConnectionManager = ElasticsearchConnectionManager

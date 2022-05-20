from dbt.adapters.elasticsearch.connections import ElasticsearchConnectionManager
from dbt.adapters.elasticsearch.connections import ElasticsearchCredentials
from dbt.adapters.elasticsearch.impl import ElasticsearchAdapter

from dbt.adapters.base import AdapterPlugin
from dbt.include import elasticsearch


Plugin = AdapterPlugin(
    adapter=ElasticsearchAdapter,
    credentials=ElasticsearchCredentials,
    include_path=elasticsearch.PACKAGE_PATH)

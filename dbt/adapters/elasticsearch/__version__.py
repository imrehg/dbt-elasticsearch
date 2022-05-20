from importlib import metadata

version: str
try:
    version = metadata.version("dbt-elasticsearch")
except metadata.PackageNotFoundError:
    version = "unknown"
finally:
    del metadata

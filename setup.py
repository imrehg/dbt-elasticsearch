#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-elasticsearch"
# make sure this always matches dbt/adapters/elasticsearch/__version__.py
package_version = "1.2.0a1"
description = """The elasticsearch adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author=<INSERT AUTHOR HERE>,
    author_email=<INSERT EMAIL HERE>,
    url=<INSERT URL HERE>,
    packages=find_namespace_packages(include=['dbt', 'dbt.*']),
    include_package_data=True,
    install_requires=[
        "dbt-core==1.2.0a1",
        <INSERT DEPENDENCIES HERE>
    ]
)

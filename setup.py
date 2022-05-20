#!/usr/bin/env python
from setuptools import find_namespace_packages, setup

package_name = "dbt-elasticsearch"
# make sure this always matches dbt/adapters/elasticsearch/__version__.py
package_version = "1.1.0"
description = """The elasticsearch adapter plugin for dbt"""

setup(
    name=package_name,
    version=package_version,
    description=description,
    long_description=description,
    author="Gergely Imreh",
    author_email="gergely@imreh.net",
    url="https://github.com/imrehg/dbt-elasticsearch",
    packages=find_namespace_packages(include=["dbt", "dbt.*"]),
    include_package_data=True,
    install_requires=[
        "dbt-core>=1,<2",
        "elasticsearch>8",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: Apache Software License",
    ],
    python_requires=">=3.7",
)

"""This file configures pytest, initializes Databricks Connect, and provides fixtures for Spark and loading test data."""

import os, sys, pathlib
from contextlib import contextmanager
sys.path.append(os.getcwd())


from pyspark.sql import SparkSession
import pytest
import json
import csv
import os
"""
except ImportError:
    raise ImportError(
        "Test dependencies not found.\n\\n nRun tests using 'uv run pytest'. See http://docs.astral.sh/uv to learn more about uv."
    )
"""


@pytest.fixture()
def spark() -> SparkSession:
    """Provide a SparkSession fixture for tests.

    Minimal example:
        def test_uses_spark(spark):
            df = spark.createDataFrame([(1,)], ["x"])
            assert df.count() == 1
    """
    try:
        
        from databricks.connect import DatabricksSession
        spark = DatabricksSession.builder.getOrCreate()
        print("DatabricksSession created successfully.")
    except ImportError as e:
        try:
            from pyspark.sql import SparkSession
            spark = SparkSession.builder.getOrCreate()
            print("SparkSession created successfully.")
        except ImportError as e:
            raise ImportError('Neither pyspark nor databricks.connect is available.')

    return spark

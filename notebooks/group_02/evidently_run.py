# Databricks notebook source
#!/usr/bin/env python3

"""
    Purpose: Run evidently tests against two comparing datasets.
"""

import sys
import os

sys.path.append(os.path.abspath("../.."))
root_dir = '/Workspace/Repos/clarissa.chevalier@artefact.com/evidently_implementation'

from src.evidently_impl import load_reference_current_data, return_data_quality_metrics, return_data_drift_metrics, return_target_drift_metrics

import pandas as pd
import numpy as np
import pytest
import json

# COMMAND ----------

path_reference = "train_01"
path_current = "train_02"

# loading reference and current data
dataset_dict = load_reference_current_data(
    path_reference=path_reference, path_current=path_current
)

# COMMAND ----------

# DATA QUALITY EVIDENTLY OUTPUT
return_data_quality_metrics(dataset_dict = dataset_dict).show(mode='inline')

# COMMAND ----------

# DATA DRIFT EVIDENTLY OUTPUT
return_data_drift_metrics(dataset_dict = dataset_dict).show(mode='inline')

# COMMAND ----------

# TARGET DRIFT EVIDENTLY OUTPUT
return_target_drift_metrics(dataset_dict = dataset_dict).show(mode='inline')

# COMMAND ----------

repo_name = "/Repos/clarissa.chevalier@artefact.com/evidently_implementation/notebooks/group_02"

# Get the path to this notebook, for example "/Workspace/Repos/{username}/{repo-name}".
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Get the repo's root directory name.
repo_root = os.path.dirname(os.path.dirname(notebook_path))

# Prepare to run pytest from the repo.
# os.chdir(f"{repo_name}")
print(os.getcwd())

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."

# COMMAND ----------



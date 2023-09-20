#!/usr/bin/env python3

"""
    Purpose: Loads json test files and performs data tests.
"""

import sys
import os

project_root_dir = os.path.abspath("../../..")
sys.path.append(project_root_dir)
root_dir = '/Workspace/Repos/clarissa.chevalier@artefact.com/evidently_implementation'

import pandas as pd
import pytest
import json

@pytest.fixture
def loading_data_quality_json_as_dict() -> dict:
    """Returns "Data Quality" results from Evidently.ai lib

    Returns:
        dict: data quality metrics.
    """

    file_path = os.path.join(root_dir,"data/output","data_quality.json")

    with open(file_path, "r") as file:
        data = json.load(file)
        
    return data


@pytest.fixture()
def loading_data_drift_json_as_dict() -> dict:
    """Returns "Data Drift" results from Evidently.ai lib

    Returns:
        dict: data drift metrics.
    """

    file_path = os.path.join(root_dir,"data/output","data_drift.json")

    with open(file_path, "r") as file:
        data = json.load(file)
        
    return data


@pytest.fixture()
def loading_target_drift_json_as_dict() -> dict:
    """Returns "Target Drift" results from Evidently.ai lib

    Returns:
        dict: target drift metrics.
    """

    file_path = os.path.join(root_dir,"data/output","target_drift.json")

    with open(file_path, "r") as file:
        data = json.load(file)
        
    return data


def test_failed_tests_percentage(loading_data_quality_json_as_dict:dict) -> None:
    """Checks whether the amount of failed tests are above 50% of the total tests.

    Args:
        loading_data_quality_json_as_dict (dict): evidently output json info
    """
    #### WRITE YOUR CODE HERE 


def test_pickup_date_drift(loading_data_drift_json_as_dict: dict) -> None:
    """Checks whether the feature pickup_day data drift is above threshold. 

    Args:
        loading_data_drift_json_as_dict (dict): evidently output json info
    """
    #### WRITE YOUR CODE HERE 


def test_negative_kendall_feature_target_correlation(loading_target_drift_json_as_dict: dict) -> None:
    """Checks whether any feature in the current dataset has passed the 
    kendall test for being negatively correlated with the target.

    Args:
        loading_target_drift_json_as_dict (dict): evidently output json info
    """
    #### WRITE YOUR CODE HERE 


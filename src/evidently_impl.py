#!/usr/bin/env python3

"""
    Purpose: Run evidently tests against two comparing datasets.
"""

import sys
import os

sys.path.append(os.path.abspath(".."))

import pandas as pd

from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset

from evidently.test_suite import TestSuite
from evidently.test_preset import DataQualityTestPreset


def load_reference_current_data(path_reference: str, path_current: str) -> dict:
    """Loads file from database and returns reference and current dataset
    for comparisson.

    Returns:
        dict: dict with both datasets.
    """

    COLUMN_NAMES = [
        "vendor_id",
        "passenger_count",
        "pickup_longitude",
        "pickup_latitude",
        "dropoff_longitude",
        "dropoff_latitude",
        "target",
        "pickup_month",
        "pickup_day",
        "pickup_hour",
    ]

    dataset_dict = {}
    for name, path in zip(["reference", "current"], [path_reference, path_current]):
        dataset = pd.read_csv(
            f"/Workspace/Repos/clarissa.chevalier@artefact.com/evidently_implementation/data/processed/{path}.csv"
        )

        dataset_sample = dataset.sample(n=5000, replace=False)
        dataset_sample = dataset_sample[COLUMN_NAMES]
        dataset_dict[name] = dataset_sample

    return dataset_dict


def return_data_quality_metrics(dataset_dict: dict) -> None:
    """Returns data quality checks

    Args:
        dataset_dict (dict): dict with both datasets.
    """
    # data quality
    data_quality_test_suite = TestSuite(
        tests=[
            DataQualityTestPreset(),
        ]
    )

    data_quality_test_suite.run(
        reference_data=dataset_dict["reference"], current_data=dataset_dict["current"]
    )
    data_quality_test_suite.save_json(
        "/Workspace/Repos/clarissa.chevalier@artefact.com/evidently_implementation/data/output/data_quality.json"
    )

    return data_quality_test_suite


def return_data_drift_metrics(dataset_dict: dict) -> None:
    """Returns data drift metrics

    Args:
        dataset_dict (dict): dict with both datasets.
    """
    # data drift
    report = Report(metrics=[DataDriftPreset()])
    report.run(
        reference_data=dataset_dict["reference"], current_data=dataset_dict["current"]
    )
    report.save_json(
        "/Workspace/Repos/clarissa.chevalier@artefact.com/evidently_implementation/data/output/data_drift.json"
    )

    return report


def return_target_drift_metrics(dataset_dict: dict) -> None:
    """Returns target drift metrics

    Args:
        dataset_dict (dict): dict with both datasets.
    """
    # target drift
    num_target_drift_report = Report(
        metrics=[
            TargetDriftPreset(),
        ]
    )

    num_target_drift_report.run(
        reference_data=dataset_dict["reference"], 
        current_data=dataset_dict["current"]
    )
    num_target_drift_report.save_json(
        "data/output/target_drift.json"
    )

    return num_target_drift_report


def create_all_presets_metrics():
    """Run all presets metrics
    """

    path_reference = "train_01"
    path_current = "train_02"

    dataset_dict = load_reference_current_data(
        path_reference=path_reference, path_current=path_current
    )

    # data quality checks
    return_data_quality_metrics(dataset_dict)

    # data drift checks
    return_data_drift_metrics(dataset_dict)

    # target checks
    return_target_drift_metrics(dataset_dict)


if __name__ == "__main__":
    create_all_presets_metrics()

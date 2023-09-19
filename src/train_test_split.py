#!/usr/bin/env python3

"""
    Purpose: Extracts subset of the dataset
"""

import sys
import os

sys.path.append(os.path.abspath(".."))

import pandas as pd
import numpy as np

if __name__ == '__main__':

    # train
    train = pd.read_csv('data/raw/train.csv')
    train['pickup_datetime'] = pd.to_datetime(train.pickup_datetime)
    train['pickup_month'] = train.pickup_datetime.dt.month
    train['pickup_day'] = train.pickup_datetime.dt.day
    train['pickup_hour'] = train.pickup_datetime.dt.hour
    train.rename(columns={'trip_duration': 'target'}, inplace=True)
    train = train.sort_values(by='pickup_datetime')
    train = train.drop(columns=['pickup_datetime','dropoff_datetime'])


    length = int(train.shape[0]/5)

    for i,j in enumerate(range(1,6)):
        subset = train[length*i:length*j]
        subset.to_csv(f'data/processed/train_0{j}.csv', index=False)
        print(subset.shape)

    min_target = train['target'].min()
    max_target = train['target'].max()

    # pred
    pred = pd.read_csv('data/raw/test.csv')
    pred['pickup_datetime'] = pd.to_datetime(pred.pickup_datetime)
    pred['pickup_month'] = pred.pickup_datetime.dt.month
    pred['pickup_day'] = pred.pickup_datetime.dt.day
    pred['pickup_hour'] = pred.pickup_datetime.dt.hour
    pred['prediction'] = np.random.normal(0, max_target+5, pred.shape[0])
    pred = pred.sort_values(by='pickup_datetime')
    pred = pred.drop(columns=['pickup_datetime'])
    pred.to_csv('data/processed/pred.csv', index=False)
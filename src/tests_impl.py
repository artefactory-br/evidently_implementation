#!/usr/bin/env python3


    Purpose:  Run production-ready test on evidently-gathered metrics.


import sys
import os

sys.path.append(os.path.abspath(..))

import pandas as pd
import pytest

df = pd.read_json('data/target_drift.json')
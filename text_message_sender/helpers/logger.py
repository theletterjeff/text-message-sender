"""Logs previous runs in a .csv file.
Used when scheduling recurring text message
sends--checks to see when the last run was,
sets sleep timer accordingly."""

import csv
from datetime import datetime
import os

import pandas as pd

def log_run(*data):
    """Log run time in csv.
    *data is typically the content of the sent text message."""
    now = datetime.now()
    if not os.path.isdir('temp'):
        os.mkdir('temp')
    with open('temp/run_log.csv', 'a+', newline='', encoding='utf-8') as run_log:
        log_writer = csv.writer(run_log, delimiter=',')
        log_writer.writerow([now, *data])

def get_last_run():
    """Find when last run occurred"""
    if os.path.isfile('temp/run_log.csv'):
        run_log = pd.read_csv('temp/run_log.csv')
        last_run = pd.to_datetime(run_log.iloc[-1, 0])
    else:
        last_run = datetime.now()
    return last_run

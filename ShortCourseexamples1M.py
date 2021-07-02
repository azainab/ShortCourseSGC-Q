import time
import signal
import numpy as np
import os
import csv
import pandas as pd
import itertools as it

import multiprocessing as ms
import threading
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
from datetime import datetime
from functools import partial

df = pd.read_csv('/lustre/home/amzaina65/ShortCourse/sampledata1M.csv')
#count = df.count()
#print("Count of data records", count)

count_meters = df['meter'].unique()
print("Count of unique meters", count_meters)

time1 = time.time()
for i in count_meters:
    meter_df = df[df.meter == i]
    print("count of meter " % i, meter_df.count())
print("total time taken", time.time() - time1)
  
  
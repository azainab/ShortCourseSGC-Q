import time
import signal
import numpy as np
import os
import csv
import pandas as pd
import itertools as it


df = pd.read_csv('/lustre/home/amzaina65/ShortCourse/sampledata1000M.csv')
time1 = time.time()
count = df.count()
print("Count of data records", count)
print("time to count the records", time.time() - time1)

  

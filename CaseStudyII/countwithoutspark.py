import time
import signal
import numpy as np
import csv
import pandas as pd

df = pd.read_csv('/lustre/home/amzaina65/ShortCourse/sampledata500M.csv')
time1 = time.time()
count = df.count()
print("Count of data records", count)
print("time to count the records", time.time() - time1)

  

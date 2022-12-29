'''import os
import concurrent.futures
import time
import win32api
start=time.perf_counter()

availableDrive=win32api.GetLogicalDriveStrings()
#print(availableDrive)
Drives=[drivestr for drivestr in availableDrive.split('\000') if drivestr]

#drives=drives.split('\000')[:-1]
#to find the files in the system
def find_files(filename, search_path):
    result = []
    # Walking top-down through all the folders in drives
    for root, dir, files in os.walk(search_path):
        #checking whether the file matches or not with existing files in the system
        if filename in files:
            result.append(os.path.join(root, filename))     #to append filename and path to a list
    return result

input_file='sample.txt'
#To acheieve multi threading,use concurrency,means parallel execution
with concurrent.futures.ThreadPoolExecutor() as executor:
    results=[executor.submit(find_files,input_file,drive) for drive in Drives]
    print(results)
    for r in concurrent.futures.as_completed(results):
        print(r.result())


finish=time.perf_counter()
print(f"time {finish-start} seconds")


finish = time.perf_counter()

print(f'Finised in {finish - start} seconds')'''
'''from chandu.teja import lahya
lahya.f()'''
import numpy as np
import pandas as pd
dates = pd.date_range("20130101", periods=6)

print(dates)

# random float values
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)
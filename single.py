import os #To interact with the under lying Operating System.
import time#Here to calculate the time taken by the process.
import win32api#To Get the all the drives in our system.
start=time.perf_counter()#To start the timer.
def find_files(filename, search_path):
    result = []
    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        #for loop is used to search the files by walking through all the folders of drive
        if filename in files:#here iam sending all the files to filename
            result.append(os.path.join(root, filename))#filename and root will be appended to result list
    return result#returning result
for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:#to get all the drives available in our system
    print(find_files("sample.txt", drive))#here iam calling the method called find_files it walks through the all drive and displays that file particular path
finish=time.perf_counter()
print(f"time {finish-start} seconds")
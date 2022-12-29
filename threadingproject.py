import re
import threading
import win32api
import os
import time

start=time.perf_counter()
def find_file(root_folder, rex):
    l =[]
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                l.append(os.path.join(root, f))
                print(l)

                     # if you want to find only one

def find_file_in_all_drives(file_name):
        # create a regular expression for the file
    rex = re.compile(file_name)

    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        threads=threading.Thread(target=find_file,args=[drive,rex])
        threads.start()

print(find_file_in_all_drives("sample.txt"))
end=time.perf_counter()
print(end-start)
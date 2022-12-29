import concurrent.futures
import os
import re
import win32api
import  time
def find_file(root_folder, rex):
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                print(os.path.join(root, f))
def find_file_in_all_drives(file_name):
    # create a regular expression for the file
    s = time.perf_counter()
    rex = re.compile(file_name)
    l=[]
    with concurrent.futures.ThreadPoolExecutor() as ex:
        tr=[ex.submit(find_file,drive,rex)for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]
    for i in concurrent.futures.as_completed(tr):
        i.result()


find_file_in_all_drives("sample.txt")
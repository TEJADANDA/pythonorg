import os
import re
import win32api
import UploadFiles
import concurrent.futures

# Using multithreading,the class FindFilelocation searches for a file on our local drives.
#This class uses UploadFilesToDB to save the SearchEngine in a SQL database.
class FindFileLocation:

    # To find a file on our local drive,we use the method find file.
    #Drive and filename are accepted parameters for this method.
    def find_file(self, root_folder, rex):
        for root, dirs, files in os.walk(root_folder):
            for f in files:
                result = rex.search(f)
                if result:
                    print("File name: {} - File location: {}".format(f, root))
                    #print("File location: {}".format(root))
                    # call to method insert_file_search_results to upload Search Engine to db
                    self.insert_file_search_results(root, f, 0)
                    break  # if you want to find only one

    # To obtain a list of all the drives in our local system or VM,use find file in all drives method.
    def find_file_in_all_drives(self, file_name):
        # For the file,create a regular expression.
        rex = re.compile(file_name)

        drives = [drivestr for drivestr in  win32api.GetLogicalDriveStrings().split('\000')[:-1]]
        print(drives)
        # To acheieve multithreading,use concurrency
        with concurrent.futures.ThreadPoolExecutor() as executor:
            [executor.submit(self.find_file, drive, rex) for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]]

    # In the  class UploadFilestoDB,the method upload file results todb is called by the method insert file search results.
    def insert_file_search_results(self, fileLocation, fileName, searchCount = 0):
        uploadObject.upload_file_results_todb(fileName, fileLocation, searchCount)

    # To Search for files in a database,use the method search forfile indb
    # Takes the filename as input.
    # This method internally call method search_in_db_for_file which is in class UploadFilesToDB
    def search_forfile_indb(self, fileName):
        # To search for a file result in a database,call the method search_forfile_indb
        searchstatus=uploadObject.search_in_db_for_file(fileName)
        if(searchstatus):
            print("File search results from local drives")
            self.find_file_in_all_drives(fileName)

# Calls for class objects
locationObject = FindFileLocation()
uploadObject = UploadFiles.Updating_DB()
fileToSearch = input()
locationObject.search_forfile_indb(fileToSearch)
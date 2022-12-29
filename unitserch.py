import unittest
import UploadFiles
#import search files
import pyodbc

server = 'HCL-02-46\SQLEXPRESS'
database = 'SearchEngine'
username = 'admin'
password = 'teja@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()


class test_capstone(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_upload_file_results_todb(self):
        uploadObj = UploadFiles.Updating_DB()
        #newfileob= search files.FindFileLocation()
        uploadObj.upload_file_results_todb("shubjb.txt",
                                           "A:\tej\sunny\ragulu\hya\shubjb.txt",0)
        # uploadObj.upload_file_results_todb("test.txt","C:\\Users\\user697\\PycharmProjects\\pythonProject\\testdata\\test.txt", 0)

        values_1 = cursor.execute(
            ''' select * from SearchEngine_Table where NameOfFile = 'shubjb.txt' ''')

        # values_2 = cursor.execute(''' select * from FileSearchResults_ta
        # le where NameOfFile = 'test.txt' ''')
        for fileInfo in values_1:
            self.assertEqual(fileInfo.NameOfFile, "shubjb.txt")
            self.assertEqual(fileInfo.File_Location, "A:\tej\sunny\ragulu\hya\shubjb.txt")

    def test_search_in_db_for_file(self):
        searchObj = UploadFiles.Updating_DB()
        searchObj.search_in_db_for_file('shubjb.txt')
        value_1 = cursor.execute(''' select * from SearchEngine_Table where NameOfFile = 'A:\tej\sunny\ragulu\hya\shubjb.txt' ''')
        for fileInfo in value_1:
            self.assertEqual(fileInfo.NameOfFile, 'shubjb.txt')

    """ def test_update_file_searchcount(self):
        searchCountObj = UploadFiles.Updating_DB()
        searchCountObj.update_file_searchcount('mobile.txt')
        values = cursor.execute(''' select * from SearchEngine_Table where NameOfFile ='mobile.txt' ''')
        for fileInfo in values:
            fileSearchCount = fileInfo.SearchCount
            print(fileSearchCount)

            fileinfoQuery = cursor.execute(''' Update SearchEngine_Table SET SearchCount = {0} WHERE NameOfFile = {1} ''')
            updateQuery = fileinfoQuery.format(fileSearchCount + 1, 'mobile.txt')
            cursor.execute(updateQuery)
            # commits data to DB

            #self.assertEqual(fileInfo.SearchCount, 9)"""


if __name__ == "__main__":
    unittest.main()
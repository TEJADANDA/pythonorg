import pyodbc
class dbpr:


    def show_file_search_results_fromdb(self):
        values = self.cursor.execute('select * from FileSearchResults_table')
        for fileInfo in values:
            print("File Name: {}".format(fileInfo.NameOfFile))
            print("File Location: {}".format(fileInfo.File_Location))

    def upload_file_results_todb(self,fileName, fileLocation, searchCount):
        query = '''  
                    INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                    VALUES
                    ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        self.cursor.execute(insertQuery)
        self.cnxn.commit()
        print("New file search results committed to DB")

    # searches for a file in db
    # Input : Filename (string)
    # output : True or False (Boolean)
    def search_in_db_for_file(self,fileName):
        # select query
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = self.cursor.execute(searchQuery)
        if (values):
            for fileInfo in values:
                print("==========================")
                print("File name: {}".format(fileInfo.NameOfFile))
                print("File path: {}".format(fileInfo.File_Location))
                print("==========================")
            return True
        return False


    def upload_file_results_todb(self, fileName, fileLocation, searchCount):
        query = '''  
                          INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                          VALUES
                          ('{0}',{1},'{2}')  '''

        insertQuery = query.format(fileLocation, searchCount, fileName)
        self.cursor.execute(insertQuery)
        self.cnxn.commit()
        print("New file search results committed to DB")


# searches for a file in db
# Input : Filename (string)
# output : True or False (Boolean)
    def search_in_db_for_file(self, fileName):
        # select query
        query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
        searchQuery = query.format(fileName)
        values = self.cursor.execute(searchQuery)
        if (values):
            for fileInfo in values:
                print("==========================")
                print("File name: {}".format(fileInfo.NameOfFile))
                print("File path: {}".format(fileInfo.File_Location))
                print("==========================")
            return True
        return False
import pyodbc
class lahya:
    def __init__(self):
        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-46\SQLEXPRESS;DATABASE=lokesh;UID=admin;PWD=teja@123')
        cursor = cnxn.cursor()
    def create_table(self,emp_id,name,salary):
        query=''' INSERT INTO lokesh_table(emp_id int ,
                                           name varchar(50),
                                           salary int) '''
        self.cursor.execute(query)
        self.cnxn.commit()

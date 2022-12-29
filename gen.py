i=1
j=1
while(i<=5):
    print("teluskoo",end="")
    j=1
    while(j<=5):
        print("rocks",end="")
        j=j+1
    i=i+1
    print()
k=ord("A")
n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(k),end="")
    k=k+1

n=int(input())
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end="")
    print()

class car:
    def __init__(self,colour,speed):
        self.colour=colour
        self.speed=speed
        self.current_speed=80
        print(colour,speed)
    def car_engine(self,engine):
        if engine==1:
            print("car is started")
        else:
            print("car is not started")
    def sound_horn(self):
        if self.engine==1:
            print("beep beeep")
        else:
            print("not started")
    def start_engine(self):
        if(self.speed>0):
            print("engine is started==true")
        else:
            print("engine is started==false")
    def stop_engine(self):
        if self.speed==0:
            print("engine is not started==true")
        else:
            print("engine is not started==false")
    def apply_brakes(self,brake):
        if brake==1:
            print("speed is decreasing")
        elif(brake==0):
            print("speed not changed")



obj=car("blue",5644)
obj.start_engine()
obj.apply_brakes(1)



import pyodbc

server = 'HCL-02-18\SQLEXPRESS'
database = 'FileSearchResults'
username = 'vyshu'
password = 'Vyshu@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

def show_file_search_results_fromdb():
    values = cursor.execute('select * from FileSearchResults_table')
    for fileInfo in values:
        print("File Name: {}".format(fileInfo.NameOfFile))
        print("File Location: {}".format(fileInfo.File_Location))

def upload_file_results_todb(fileName, fileLocation, searchCount):
    query = '''  
                INSERT INTO FileSearchResults_table (File_Location, SearchCount, NameOfFile)
                VALUES
                ('{0}',{1},'{2}')  '''

    insertQuery = query.format(fileLocation, searchCount, fileName)
    cursor.execute(insertQuery)
    cnxn.commit()
    print("New file search results committed to DB")

# searches for a file in db
# Input : Filename (string)
# output : True or False (Boolean)
def search_in_db_for_file(fileName):
    # select query
    query = ''' select * from FileSearchResults_table where NameOfFile = '{0}' '''
    searchQuery = query.format(fileName)
    values = cursor.execute(searchQuery)
    if(values):
        for fileInfo in values:
            print("==========================")
            print("File name: {}".format(fileInfo.NameOfFile))
            print("File path: {}".format(fileInfo.File_Location))
            print("==========================")
        return True
    return False
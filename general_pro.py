import pyodbc
import Data

# Hardcoded Global variables used connect to DB
server = 'HCL-02-18\SQLEXPRESS'
database = 'Employee_details'
username = 'vyshu'
password = 'Vyshu@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class Notinlist(Exception):
    pass
class sameproject(Exception):
    pass

class bonuserror(Exception):
    pass
class suresherror(Exception):
    pass
class IdnotexistError(Exception):
    pass


class Employee:
    project=['python','c','java']
    bonus=2
    def _init_(self,Name,Emp_Id,Salary,Project):
        self.Name=Name
        self.Emp_Id=Emp_Id
        self.Salary=Salary
        self.Project=Project
    def tablecreation(self):
        createobj.creating_table()
    def insert_Emp_Details(self):
        query='''  
                    INSERT INTO Employee_details_table (Name,Emp_Id,Salary,Project)
                    VALUES
                    ('{0}',{1},{2},'{3}')  '''
        insert_query=query.format(self.Name,self.Emp_Id,self.Salary,self.Project)
        cursor.execute(insert_query)
        cnxn.commit()
        print("Employee details commited to db")

    def Display_Emp_Details(self):

        query='''select * from Employee_details_table where Name = '{0}' '''
        searchquery=query.format(self.Name)
        values=cursor.execute(searchquery)
        for fileinfo in values:
            print("details from DB")
            print("Name={}".format(fileinfo.Name))
            print("Emp_Id={}".format(fileinfo.Emp_Id))
            print("Salary={}".format(fileinfo.Salary))
            print("Project={}".format(fileinfo.Project))

    def add_bonus(self):
        try:
            bonus=int(input())
            if bonus>2:
                raise bonuserror
            elif bonus<0:
                raise suresherror
            else:
                query = ''' select * from Employee_details_table where Name='{}' '''
                searchquery = query.format(self.Name)
                values = cursor.execute(searchquery)
                for Info in values:
                    print(Info)
                    oldsalary = Info.Salary
                    newsalary = oldsalary * (1 + bonus)
                    print(newsalary)
                    query1 = ''' UPDATE Employee_details_table SET Salary={0} WHERE Name='{1}' '''
                    query2 = query1.format(newsalary, self.Name)
                    # print(query2)
                    cursor.execute(query2)
                    # print(query2)
                    cnxn.commit()
        except bonuserror:
            print("bonus should not be gretarthan 2")
        except suresherror:
            print("bonus should not be less than 0")

        except:
            pass
    def update_salary(self):
        try:
            salary = int(input())
            query = ''' select * from Employee_details_table where Name='{}' '''
            searchquery = query.format(self.Name)
            values = cursor.execute(searchquery)
            for Info in values:
                oldsalary = Info.Salary
                query = '''UPDATE Employee_details_table SET Salary={0} WHERE Name='{1}' '''
                query1 = query.format(salary, self.Name)
                cursor.execute(query1)
                cnxn.commit()
        except:
            pass

    def change_project(self):
        new_project = input()
        try:
            query = '''select * from Employee_details_table where Name='{0}' '''
            searchquery = query.format(self.Name)
            values = cursor.execute(searchquery)
            for fileinfo in values:
                oldproject = fileinfo.Project
                if new_project == oldproject:
                    raise sameproject
                elif (new_project not in self.project):
                    raise Notinlist
                else:
                    query = '''UPDATE Employee_details_table SET Project='{0}' WHERE Name='{1}' '''
                    query1 = query.format(new_project, self.Name)
                    cursor.execute(query1)
                    cnxn.commit()
                    print("congrats ,your in new project")
        except Notinlist:
            print("Not in the list of projects")
        except sameproject:
            print("oops,again you are in same project")

        except:
            pass

    def delete_Emp_details(self):
        try:
            input1 = int(input())
            query = '''select * from Employee_details_table'''
            values = cursor.execute(query)
            l = []
            for info in values:
                l.append(info.Emp_Id)
                if input1 in l:
                    query = '''delete from Employee_details_table where Emp_Id={} '''
                    query1 = query.format(input1)
                    values1 = cursor.execute(query1)
                    cnxn.commit()
                else:
                    raise IdnotexistError
        except IdnotexistError:
            print("Emp_Id is not in the DB")
        except:
            pass

createobj=Data.Employee_schema()
obj=Employee("Nandhu",619,200000,"Java")
#obj.insert_Emp_Details()
#obj.delete_Emp_details()
#obj.Display_Emp_Details()
obj.add_bonus()
#obj.update_salary()
#obj.change_project()
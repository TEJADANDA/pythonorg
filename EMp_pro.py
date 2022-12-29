class insertexception(Exception):
    def _str_(self):
        return "project name not in list of the projects"
class id_exception(Exception):
    def _str_(self):
        return "id already exist, enter new id for employee"
class bonus_ex(Exception):
    def _str_(self):
        return "bonus is very high ,enter with in range"
class schema:
    def _init_(self):
        # In this connection string server,database,user Id and password is included.
        # for connnecting database to perform operations on Database table.
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=HCL-02-46\SQLEXPRESS;DATABASE=employee_projects;UID=admin;PWD=teja@123')
        self.cursor = self.cnxn.cursor()

    def create_table(self):
        query = '''  CREATE TABLE employee_projects ( emp_id int NOT NULL,
                                                 name varchar(50) NOT NULL,
                                                 salary int NOT NULL,
                                                 project varchar(50) NOT NULL,
                                                  PRIMARY KEY (emp_id));  '''
        self.cursor.execute(query)
        self.cnxn.commit()
import pyodbc
server = 'HCL-02-46\SQLEXPRESS'
database = 'FileSearchResults'
username = 'admin'
password = 'teja@123'
cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cors = cnxn.cursor()
class EMPLOYEE:
    project=['c','java','python']
    def add_employee_details(self,id,name,salary,project):
        query_for_search_id=''' select emp_id from employee_projects  '''
        format_query_for_search_id= query_for_search_id.format(id)
        value_of_query_for_search_id=cors.execute(format_query_for_search_id)
        f=False
        for i in value_of_query_for_search_id:
            if i.emp_id == id:
                f=True
                break
        if f:
            try:
                raise id_exception
            except id_exception as id_ex:
                print(id_ex)
        else:
            query = '''  INSERT INTO employee_projects (emp_id,name,salary,project) values ({0},'{1}',{2},'{3}') '''
            insertquery = query.format(id, name, salary, project)
            if project in project:
                cors.execute(insertquery)
                cnxn.commit()
                print("details insert successfully in db")
            else:
                try:
                    raise insertexception
                except insertexception as ex:
                    print(ex)
    def update_details(self,id,project='',salary=0):
        if salary !=0:
            query_for_salary_uptate= ''' UPDATE employee_projects SET salary = {0} where emp_id = {1} '''
            insertquery_for_salary_update=query_for_salary_uptate.format(salary,id)
            cors.execute(insertquery_for_salary_update)
            cnxn.commit()
            print("updated successfully")
        if project:
            query_for_project= ''' UPDATE employee_projects SET project = '{0}' where emp_id = {1} '''
            insertquery_for_project_update = query_for_project.format(project, id)
            cors.execute(insertquery_for_project_update)
            cnxn.commit()
            print("update successfully")
    def display_employee_details(self):
        query_for_display_details='''select * from employee_projects '''
        values=cors.execute(query_for_display_details)
        for i in values:
            print("employee id ",i.emp_id," employee name ",i.name," salary ",i.salary," project ",i.project)
    def delete_employee_details(self,id):
        query=''' DELETE from employee_projects where emp_id = {0}   '''.format(id)
        cors.execute(query)
        cnxn.commit()
        print("deleted successfully")
    def add_bonus(self,id,bonus):
        if bonus > 0 and bonus <= 2:
            query = ''' select salary from employee_projects where emp_id = {}'''.format(id)
            value = cors.execute(query)
            for i in value:
                salary = i.salary
            bonus_and_bonus = salary + salary * bonus
            query_for_update_bonus = ''' UPDATE employee_projects SET salary = {0} where emp_id = {1} '''.format(
                bonus_and_bonus, id)
            cors.execute(query_for_update_bonus)
            cnxn.commit()
            print("bouns updated successfully")
        else:
            try:
                raise bonus_ex
            except bonus_ex as ex:
                print(ex)

obj=EMPLOYEE()
obj.add_employee_details(52130547,'D.TEJA',200000,'python')
obj.update_details(52130547,project='java')
obj.display_employee_details()
obj.delete_employee_details(52130547)
obj.add_employee_details(52130547,'D.TEJA',200000,'java')
obj.add_bonus(52130547,1)
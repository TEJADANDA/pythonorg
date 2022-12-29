''''def div(a,b):
    #try:
    d=a/b
    print(d)

    #except:
        #print("not divisble by zero")

div(1,"l")'''
class negativevalueerror(Exception):
    def __str__(self):
        return "hvhkvlvj"

class Highvalueerror(Exception):
    def __str__(self):
        return "entered amount is greater than availble balance"

class Bank:
    def __init__(self,account_num,name,balance):
        self.account_num=account_num
        self.name=name
        self.balance=balance

    def depoist(self,limit):
        try:
            if limit<=2000:
                self.balance=self.balance+limit
                print("amount is depoisted",self.balance)
            else:
                raise negativevalueerror
        except negativevalueerror as ex:
            print(ex)


    def withdraw(self,entered):
            try:
                if(entered<=self.balance):
                    print("amount is withdrwan,available balance is",self.balance-entered)

                else:
                    raise Highvalueerror
                    print("avaiable balance is",self.balance)
            except Highvalueerror as ex:
                print(ex)


obj=Bank(3329828883902930,"teja",20000)
obj.depoist(2000)
obj.withdraw(2000)

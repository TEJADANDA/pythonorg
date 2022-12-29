class lift:
    def __init__(self,lift,destination,teja):
        self.lift=lift
        self.destination=destination
        self.teja=teja
    def press_button(self):
        if self.teja<self.lift:
            for i in range(self.teja,self.lift+1,-1):
                print("lift is coming",i)

obj=lift(5,8,2)
obj.press_button()
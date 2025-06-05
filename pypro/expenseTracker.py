class Expensetracker():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def spend(self,utilities,price):
        self.salary-=price
        print("your spend on {} - Rs{}:{}".format(utilities,price,self.salary))
        print(self.salary);
        




first_person=Expensetracker('shashi',2000)
first_person.spend('biscuits',50)
first_person.spend('chocolate',150)
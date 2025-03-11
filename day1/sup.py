class Person(object): #parent class

    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def  display(self):
        print(self.name)
        print(self.age)

class employee(Person):
     
    def __init__(self,id,address,name,age):
        super().__init__(name,age)
        self.id=id
        self.address=address

        

e=employee(1234,'india','vanshi',20)
e.display()

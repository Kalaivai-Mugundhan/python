class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def info(self):
        print(f" i am cat, my name is {self.name} , i am {self.age} years old" )
    def sound(self):
        print("i make sound meow...")

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age 

    def info(self):
        print(f" i am dog, my name is {self.name} , i am {self.age} years old" )
    def sound(self):
        print("i make sound barking...")

c=cat('kitty',5)
d=dog('puppy',8)

for pets in (c,d):
    pets.info()
    pets.sound()
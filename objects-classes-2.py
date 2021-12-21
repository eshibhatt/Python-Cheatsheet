#declaring a class
class Robot:
    #adding a constructor
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    #adding a method
    def intro_self(self):
        print("I am "+self.name)
    
#declaring an object to a class
r1=Robot("Tom","Blue")
r2=Robot("Jerry","Brown")   

class Person:
    def __init__(self,Name,Personality,i):
        self.name=Name
        self.personality=Personality
        self.is_sitting=i
    def sit_down(self):
        self.is_sitting=True
    def stand_up(self):
        self.is_sitting=False

p1=Person("Alice","aggressive",False)
p2=Person("Robert","kind",True)

#adding another class' object as data to an object

p1.robot_owned=r2
p2.robot_owned=r1
'''NOTEE-The above can also be accomplised, by adding another parameter
to the constructor, then passing the value as argument, while declaring the object'''

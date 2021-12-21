class person():
    def __init__(self,name,blood):
        self.name=name
        self.blood=blood
    def data(self):
        print('{} {}'.format(self.name,self.blood))

p1=person('Rayn','O-ve')

#To create a class that inherits the functionality from another class, send the parent class as a parameter
#the child class will have the same properties and methods as its parent class
class student(person):
    #When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    def __init__(self,name,blood):
        Person.__init__(self,name,blood) #to retain the parent's __init__
        super().__init__(name,blood) #make inherit all props and methods from the parent
        self.graduationyear = 2024 #adding a property to child
        
        #new methods can also be added to the child class

s1=student('Daisy','O+ve')
print(s1.data())

        
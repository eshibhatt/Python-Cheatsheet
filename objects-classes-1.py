#creating a class
'''class definitions cannot be empty, 
but if you for some reason have a class defined without any statements,
put in the 'pass' keyword to avoid getting an error.'''

class students:
    #instance variables
    branch=5
    #constructors
    def __init__(self,first:int,last:int,rno)-> None: # -> is used to document the return type of the function
        self.first=first
        self.last=last
        self.rno=rno
    
    #Regular Methods= takes the instance/object as 1st argument (self)
    def read(self):
        print("Student is reading")
    
    #Class Methods= takes the class as its 1st argument (cls); they are alternate constructors
    @classmethod
    def slide(cls,branch):
        cls.branch=branch
    
    #Static methods- takes no arguments.
    import datetime
    @staticmethod
    def is_classDay(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        else:
            return True

#declaring objects
S1=students('terry','cruise','3')
S2=students('Rose','roberts','4')
S3=students('James','Alias','5')

#declaring object attribute without a declared constructor
S3.statehood='Britain'

#accessing by object
print(S3.statehood)
print('{} {}'.format(S1.first,S1.last))
S1.read()

#accessing data/methods by class
print(students.branch)
students.slide(4)
students.read(S1)
print(students.__dict__)



#deleting object properties
del S3.statehood
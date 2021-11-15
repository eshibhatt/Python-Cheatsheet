# python supports multiple assignments
x=y=z=10
a,b,c= 10,20,30

#input options
name=input("what is your name?") #takes a string
age=int(input('what is your age?')) #explicitly converts the input string into int then assigns
length,height,width=map(int,input('enter the dimensions').split()) #takes space separated int values

#output options
print(a) #variable
print('hello world') #string
print('a',2+5,b) #multiple comma separated operations
print(b,a,sep="@") #changes the default sep from space to @
print(a,end="@") #changes newline character with a, and puts in one line
print(b)

#operations in py
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a**b) #exponentiation
print(a/b)  #division (always returns a float value)
print(a%b)  #returns the remainder
print(a//b) #returns the quotient

#unary operators
a+=a #same as a=a+1
a-=a #same as a=a-1

'''

relational operators (returns only boolean values, i.e. true/false)
<,<=,>=,==,!=

logical operators
and- when both are true (like set's intersection)
or- when either is true (like set's union)
not- gives true if the argument evaluates to be false (like set's complement)
    a=9
    if not(a%3==0 or a%5==0):
        print('returns false, as the eq evaluates to be true')

'''
#a basic function
''' here x,y has local scope, thus these identifiers can be used globally for other purposes
    y is a default parameter, i.e. if value of y is not given,
    python will fill it with the default value assigned
    note: that its not necessary to put default assignments
    but rather a failsafe as in the client forgets passing the second variable into the function'''

def oper(x,y=3):
    return x+y,x-y,x*y,x/y  #returning mutliple values

a=int(input('enter a number='))
b=int(input('enter another number='))
add,sub,mult,div=oper(a,b) #calling the function and storing the returned objects in different variables
print(add,sub,mult,div)
#a basic py code, to demonstrate flow of control in py
'''Demonstrations for relational and logical operators have been made too'''

runs=int(input('enter a number='))

if runs>=200:
    print('Batsman scored a double CENTURY')
elif runs>=100: #checks for this condition, only if the condition before fails
    print('Batsman scored a CENTURY')
elif runs>100 and runs<200: # there can be as many elif u want
    print('Hold up! we are nearing a Double century')
elif (runs>50 and runs<100) or runs>300:
    print('THIS IS INTENSE')
else:    #executes when the variable meets none of the defined conditions before
    print('We are doomed')



#Jump Statements
#    Break: terminates the rest of the loop and jumps to the 1st statement outside the loop
a=int(input())
b=int(input())

while a>b:
    if b==0:
        print('0 division error')
        break #goes from here to
    else:
        print(a/b)
        a-=a
    print('terminated') # down here

# Continue: forces the next iteration of the loop to start from begin
a=int(input())
b=int(input())

for i in range(0,10): #up here, iterated for the next run
    if b==0: 
        print('0 division error')
        continue  #goes from here to
    else:
        print(a/b)
    print('terminated')
#for loop
''' 1. It is self-incrementing
    2. the conditional variable need not be declared before use
    3. runs as long as the sequence/range is not traversed fully
'''
for i in range(0,10,2):    #on a range, targeting even nos. range(start,end,sep)
    print(i)

for i in [1,2,3]:    #on a sequence
    print(i)
else:                #optional loop-else can also be used in while loop
    print('ending loop after printing all elements in list')


#while loop
''' 1. the conditional variable in while loop needs to be declared prior.
    2. the incrementing statement must be included to avoid an infinite loop
    3. it runs as long as the base condition is true
'''
a=5
while a<10:
    print(a)
    a=a+1


#nested loops
'''
    Loops can be nested, within loops. To understand see the below problem.
    Q.Generate an odd no of N digits, divisible by 3 but not 9.
'''

Ops= int(input()) #no of times the user wants to run this code

for i in range(0,Ops):
    N=int(input())
    L=10**(N-1) #lower limit of digit range
    U=(10**N)-1 #upper limit of digit range
    for j in range(L,U):
        if j%3==0 and j%9!=0 and j%2!=0:
            print(j)
            break
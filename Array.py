arr=['a','b','c','d']
print(arr[1])


#pop- O(1)
arr.pop()

#push- O(1)
arr.append('e')

#insert- O(n)
arr.insert(1,'o')
print(arr)

#splice
arr.insert(2,'alien')   #O(n)

print(arr)
#this code shows the different functions that can be performed on an array
#importing array for array operations
from array import *

#initialize array with array values
#The code creates an array named array1
array1 = array('i',[1,2,3,40,10,80,20,34])
#the for in loop iterates over every element in a list
for x in array1:
  print(x)

#Accessing each element of an array using the index of the element.
array2 = array('d',[10.2,3.5,7.2,4.5,78.0])
print(array2[4])

#insert operation to insert one or more elements into an array.
array3 = array('f',[5.0,2.3,1.5,3.6])
array3.insert(2,7.8)

for x in array3:
  print(x)

#deletion refers to removing en element in an array
#python in-built remove() method

array4 = array('i',[30,20,10,4,3,7])
array4.remove(4)
for x in array4:
  print(x)

#searching for an array element based on value or index
#using the index method

array5 = array('i',[30,20,10,40,90])
print(array5.index(20))

#update on array element
array6 =  array('i',[40,20,67,30,20])
array6[4] = 32

for x in array6:
  print(x)

#using the slicing operator in array
array7 =array('i', [4,6,7,2,89,30,14,67])
print(array7[2:5])
print(array7[-5])
print(array7[5:])
print(array7[:])

#using pop() to remove array value at a certain index 
array8 =array('i', [4,6,7,2,89,30,14,67])
print(array8.pop(2))


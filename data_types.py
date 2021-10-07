import numpy as np

#integers

i = 10 #integer 
print(type(i)) #print out data type of i 

a_i = np.zeros(i,dtype=int) #declare an aray of ints
print(type(a_i)) #will return ndarray
print(type(a_i[0])) #this will return int64/32

#floats
x = 119.0 #floating point number
print(type(x)) #print out the type of x

y = 1.19e2 #float 119 in scientific notation
print(type(y)) #print out the type of y 

z = np.zeros(i,dtype=np.float64) #declare an array with floats
print(type(z)) #print type of array
print(type(z[0])) # float

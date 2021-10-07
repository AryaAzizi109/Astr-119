#python exeptions let you deal with unexpected results 
try:
	print(a) #will throw an exeption because a is not defined
except:
	print("a is not defined")

#there are specific errors to help with cases 
try:
	print(a)
except NameError:
	print("a is still not defined!")
except:
	print("something else went wrong")


#this will break our program
#because a is not defined 
print(a)

#string

s = "i am a string."
print(type(s))

#Boolean

yes = True 
print(type(yes))

no = False 
print(type(no)

#list -- ordered and changeable 

alpha_list = ["a", "b", "c"]  #list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple -- order and unchangeabel

alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("we cant change elements of a tuple")
	print(alpha_tuple)
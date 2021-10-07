import numpy as np

def main():
	i = 0
	n = 10
	x = 119.0

	# we can use numpy to declare arrays quickly

	y = np.zeros(n,dtype=float)

	# we can use for loops to iterate with a variable 

	for i in range(n):
		y[i] = 2.0 * float(i) + 1.

	#we can also simply iterate through a variable
	for y_element in y:
		print(y_element)

if __name__ == "__main__":
	main()
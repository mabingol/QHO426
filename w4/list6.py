# Python program to get average of a list
def Average(list):
	return sum(list) / len(list)

# Driver Code
list = [15, 9, 55, 42, 99, 29, 63, 49, 0.043334]
average = Average(list)

# Printing average of the list
print("Average =", round(average, 5))

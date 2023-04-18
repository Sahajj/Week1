# Python prog to illustrate the following in a list
def find_len(list1):
	length = len(list1)
	list1.sort()
	print("Smallest element is:", list1[0])
# Driver Code
list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
Largest = find_len(list1)

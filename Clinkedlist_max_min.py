# Python3 program to find minimum and maximum
# value from singly circular linked list

# structure for a node
class Node:
	
	def __init__(self):
		
		self.data = 0
		self.next = None
	
# Function to print minimum and maximum
# nodes of the circular linked list
def printMinMax(head):

	# check list is empty
	if (head == None):
		return;

	# initialize head to current pointer
	current = head;

	# initialize max int value to min
	# initialize min int value to max
	min = 1000000000
	max = -1000000000;

	# While last node is not reached
	while True:

		# If current node data is lesser for min
		# then replace it
		if (current.data < min):
			min = current.data;

		# If current node data is greater for max
		# then replace it
		if (current.data > max):
			max = current.data;

		current = current.next;	
		if(current == head):
			break
	print('Minimum = {}, Maximum = {}'.format(min, max))

# Function to insert a node at the end of
# a Circular linked list
def insertNode(head, data):
	current = head;
	
	# Create a new node
	newNode = Node()

	# check node is created or not
	if not newNode:
		print("\nMemory Error");
		return head

	# insert data into newly created node
	newNode.data = data;

	# check list is empty
	# if not have any node then
	# make first node it
	if (head == None):
		newNode.next = newNode;
		head = newNode;
		return head

	# if list have already some node
	else:

		# move first node to last node
		while (current.next != head):
			current = current.next;

		# put first or head node address
		# in new node link
		newNode.next = head;

		# put new node address into
		# last node link(next)
		current.next = newNode;	
	return head

# Function to print the Circular linked list
def displayList(head):
	current = head;

	# if list is empty simply show message
	if (head == None):
		print("\nDisplay List is empty");
		return;

	# traverse first to last node
	else:
		
		while True:
			print(current.data, end=' ');
			current = current.next;		
			if(current==head):
				break
	print()

# Driver Code
if __name__=='__main__':
	
	Head = None;

	Head = insertNode(Head, 99);
	Head = insertNode(Head, 11);
	Head = insertNode(Head, 22);
	Head = insertNode(Head, 33);
	Head = insertNode(Head, 44);
	Head = insertNode(Head, 55);
	Head = insertNode(Head, 66);

	print("Initial List: ", end = '')

	displayList(Head);

	printMinMax(Head);

# This code is contributed by rutvik_56

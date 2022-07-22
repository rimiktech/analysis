class Node:

	
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:

	
	def __init__(self):
		self.head = None

	
	def pairwiseSwap(self):
		temp = self.head

	
		if temp is None:
			return

		
		while(temp and temp.next):

			
			if(temp.data != temp.next.data):

				
				temp.data, temp.next.data = temp.next.data, temp.data

		
			temp = temp.next.next


	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	
	def printList(self):
		temp = self.head
		while(temp):
		    print (temp.data),
		    temp = temp.next



llist = LinkedList()
llist.push(10)
llist.push(90)
llist.push(45)
llist.push(29)
llist.push(91)

print ("Linked list before calling pairWiseSwap() ")
llist.printList()

llist.pairwiseSwap()

print ("\nLinked list after calling pairWiseSwap() ")
llist.printList()

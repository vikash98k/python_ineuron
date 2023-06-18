class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		


def addTwoLists(first, second):
	num1= []
	num2 = []
	number1 = 0
	number2 = 0
	while first.head:
		num1.append(first.head.data)
		first.head = first.head.next
	while second.head:
		num2.append(second.head.data)
		second.head = second.head.next
	

	for i in range(len(num1)):
		if i==0:
			number1 = num1[i]
		else:
			number1 = number1*10+num1[i]
	for i in range(len(num2)):
		if i==0:
			number2 = num2[i]
		else:
			number2 = number2*10+num2[i]
	sum_nums = [int(char) for char in str(number1 + number2)]
	sum_nums.reverse()
	return sum_nums
if __name__ == '__main__':
	first = LinkedList()
	second = LinkedList()
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)
	first.push(9)


	second.push(9)
	second.push(9)
	second.push(9)
	second.push(9)

	ans = addTwoLists(first, second)
	print(ans)
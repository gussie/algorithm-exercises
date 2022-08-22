'''
Implement a min heap class, with the following methods: 
- put() -- adds a value to a heap, and returns the new heap
- get() -- removes and returns the min value from a heap

Note: Min heap is a binary tree where the min value is the root
Heap is stored as a list, where list[1] == root, list[2] == root.left, ... 
Thus a child's parent is child_position // 2


'''


import unittest, random


class Heap:
	def __init__(self, array):
		self.array = [None] # initialize with None to create 1-indexed list

	def put(self, value): 
		if len(self.array) == 1:
			self.array.append(value)
		
		else:
			self.array.append(value)
			current_pos = len(self.array) - 1 #didnt fix
			
			while current_pos > 1:
				parent_pos = (current_pos) // 2
				if self.array[current_pos] < self.array[parent_pos]:
					placeholder = self.array[current_pos]
					self.array[current_pos] = self.array[parent_pos]
					self.array[parent_pos] = placeholder
					current_pos = parent_pos
				else: 
					break


	def get_children(self, index): 
		children = []
		
		if index*2 <= len(self.array) - 1: 
			children.append(index*2)
		if index*2+1 <= len(self.array) - 1:
			children.append(index*2 + 1)

		return children


	def bubble_down(self, index): 
		while True:
			children = self.get_children(index)
			if children == []:
				break
			if len(children) == 1: 
				to_swap = children[0]
			if len(children) == 2: 
				if self.array[children[0]] < self.array[children[1]]: 
					to_swap = children[0]
				else: 
					to_swap = children[1]

			if self.array[index] < self.array[to_swap]:
				break
			else:
				placeholder = self.array[index]
				self.array[index] = self.array[to_swap]
				self.array[to_swap] = placeholder	
				index = to_swap		


	def get(self):
		if len(self.array) > 1:
			root = self.array[1] # replace root with nth value 
			self.array[1] = self.array[len(self.array) - 1]
			self.array.pop()
			self.bubble_down(1)
			return root
		else:
			return None


class TestHeap(unittest.TestCase):

	def make_heap(self, inputs):
		h = Heap(None)
		for i in inputs:
			h.put(i)
		return h


	def test_can_insert_to_heap(self):
		h = self.make_heap([4, 5, 3, 7, 2])
		self.assertEqual(h.array, [None, 2, 3, 4, 7, 5])


	def test_can_remove_value_from_heap(self):
		h = self.make_heap([4, 5, 3, 7, 2])
		smallest = h.get()
		self.assertEqual(smallest, 2)
		self.assertEqual(h.array, [None, 3, 5, 4, 7])


	def test_get_on_empty_heap(self):
		h = self.make_heap([])
		smallest = h.get()
		self.assertEqual(smallest, None)
		self.assertEqual(h.array, [None])


	def test_can_add_and_get_many_values(self):
		num = 1000

		inputs = [i+10 for i in range(num)]
		random.shuffle(inputs)

		h = self.make_heap(inputs)
		outputs = []
		for i in range(0, num):
			outputs.append(h.get())

		# assert that values are sorted in increasing order		
		inputs.sort()
		self.assertEqual(outputs, inputs)


if __name__ == '__main__':
    unittest.main()
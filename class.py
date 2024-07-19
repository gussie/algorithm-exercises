# To run: python class.py

import unittest


class Person: 

	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

	def print(self):
		print("This is %s with gender %s" % (self.name, self.gender))

	def name_swap(self, other_person):
		original_name = self.name
		self.name = other_person.name
		other_person.name = original_name


# class TestPerson(unittest.TestCase):

# 	def test_can_swap_names_of_two_persons(self):
# 		caitlin = Person("Caitlin", "F")
# 		robsie = Person("Robsie", "M")
# 		caitlin.name_swap(robsie)

# 		self.assertEqual(caitlin.name, 'Robsie')
# 		self.assertEqual(robsie.name, 'Caitlin')

# 	def test_can_swap_name_with_itself(self):
# 		caitlin = Person("Caitlin", "F")
# 		caitlin.name_swap(caitlin)

# 		self.assertEqual(caitlin.name, 'Caitlin')

def malloc(num_bytes):
	return [0] * num_bytes


class ArrayList:

	def __init__(self):
		self.array = malloc(5)
		self.array[0] = 5  # how large is the array
		self.array[1] = 0  # how large is the list

	def push(self, new_value):
		if self.array[1] + 2 == self.array[0]: 		# if list is already full
			new_array = malloc(self.array[0] * 2)  	# allocate 2x memory
			new_array[0] = self.array[0] * 2
			for i in range(1, self.array[1]+2):
				new_array[i] = self.array[i]
			self.array = new_array		

		self.array[2 + self.array[1]] = new_value
		self.array[1] += 1 

	def pop_off(self):
		self.array[1] -= 1 

	def size(self):
		return self.array[1]

	def is_empty(self):
		return self.size() == 0

	def get_values(self):
		return self.array[2: 2 + self.array[1]]


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.first = None # first Node

	def push(self, new_value):
		node = Node(new_value)

		if self.first is None:
			self.first = node
		else:
			# find last node
			last = self.first
			while last.next is not None:
				last = last.next

			last.next = node


	def pop_off(self):
		if self.first is None:
			pass

		if self.first.next is None:
			self.first = None

		else:
			node = self.first
			while node.next.next is not None:
				node = node.next
			node.next = None

	def size(self):
		count = 0
		node = self.first
		while node is not None:
			count += 1
			node = node.next
		return count

	def is_empty(self):
		return self.size() == 0

	def get_values(self):
		values = ArrayList()
		node = self.first
		while node is not None:
			values.push(node.value)
			node = node.next
		return values.get_values()


class TestList(unittest.TestCase):

	def test_new_list_is_empty(self):
		empty_list = LinkedList()
		self.assertEqual(empty_list.size(), 0)
		self.assertTrue(empty_list.is_empty())

	def test_append_and_pop_method_yield_correct_size(self):
		test_list = LinkedList()
		self.assertEqual(test_list.size(), 0)
		self.assertTrue(test_list.is_empty())

		test_list.push('Robsicle')
		self.assertEqual(test_list.size(), 1)
		test_list.push('Robsie')
		self.assertEqual(test_list.size(), 2)
		test_list.push('Robs')
		self.assertEqual(test_list.size(), 3)

		test_list.pop_off()
		self.assertEqual(test_list.size(), 2)
		test_list.pop_off()
		self.assertEqual(test_list.size(), 1)
		test_list.pop_off()
		self.assertEqual(test_list.size(), 0)

		self.assertTrue(test_list.is_empty())


	def test_append_and_pop_method_yield_correct_values(self):
		test_list = LinkedList()
		test_list.push('Robsicle')
		test_list.push('Robsie')
		test_list.push('Robs')
		test_list.push('Rob')
		test_list.push('Ro')
		test_list.push('R')
		self.assertEqual(test_list.get_values(), ['Robsicle', 'Robsie', 'Robs', 'Rob', 'Ro', 'R'])
		test_list.pop_off()
		self.assertEqual(test_list.get_values(), ['Robsicle', 'Robsie', 'Robs', 'Rob', 'Ro'])


if __name__ == '__main__':
    unittest.main()
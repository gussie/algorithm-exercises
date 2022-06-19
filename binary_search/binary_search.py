'''
Implement a binary search tree class, with the following methods: 
	def find(int)
- insert()
- delete()
- desc_ordered()

'''

import unittest
import random

class Node:
	def __init__(self, value, left, right):
		self.value = value
		self.left = left
		self.right = right
	
	def insert(self, value):
		# Adds a given value to tree. If value already present, returns False.
		if self.value == value: 
			return False
		if self.value > value: 
			if self.left != None: 
				return self.left.insert(value)
			else: 
				self.left = Node(value, None, None)
				return True
		else:
			if self.right != None: 
				return self.right.insert(value)
			else: 
				self.right = Node(value, None, None)
				return True

	def find(self, value):
		# Returns a given value if it exists in a tree; False otherwise.
		if self.value == value: 
			return value
		if self.value > value: 
			if self.left != None: 
				return self.left.find(value)
			else: 
				return False
		else:
			if self.right != None: 
				return self.right.find(value)
			else: 
				return False

	def delete(self, value):
		"""
		Deletes a given node, and returns `(root, deleted)`, where
		`root` is the (potentially new) node for subtree, and `deleted`
		indicates whether the value was found and deleted in the subtree.
		"""
 
		# Base case: we've found the node we're supposed to delete
		if self.value == value:
			# Need to delete current node and replace by
			# either max(left) or min(right) if they exist.
			if self.left is not None:
				(left_child, max_left) = self.left.delete_max() 	# TO DO - write f(x)
				return (Node(max_left, left_child, self.right), True)

			if self.right is not None:
				(right_child, min_right) = self.right.delete_min()	# TO DO - write f(x)
				return (Node(min_right, self.left, right_child), True)

			# No children
			return (None, True)

		# Recursive case: descend left or right to find value
		if value < self.value: 
			if self.left is not None: 
				(left_child, deleted) = self.left.delete(value)
				self.left = left_child
				return (self, deleted)
			else: 
				return (self, False)
		else:
			if self.right is not None: 
				(right_child, deleted) = self.right.delete(value)
				self.right = right_child
				return (self, deleted)
			else: 
				return (self, False)


	def desc_ordered(self):
		# Returns the desc-ordered list of nodes under this node.
		nodes = []
		if self.right is not None:
			nodes += self.right.desc_ordered()
		
		nodes += [self.value]

		if self.left is not None:
			nodes += self.left.desc_ordered()
		
		return nodes



class Tree:
	def __init__(self, root):
		self.root = root

	def insert(self, value): 
		if self.root is None:
			self.root = Node(value, None, None)
			return True
		else: 
			return self.root.insert(value)
	
	def find(self, value):
		if self.root is None:
			return False
		else: 
			return self.root.find(value)

	def delete(self, value):
		"""
		Deletes the given value from the tree and returns true if
		it was deleted or false if it was not found in the tree.
		"""
		if self.root is None:
			return False
		else:
			(self.root, deleted) = self.root.delete(value)
			return deleted
	
	def desc_ordered(self): 
		if self.root is None:
			return []
		else:
			return self.root.desc_ordered()


class TestTree(unittest.TestCase):
	def test_can_build_and_print_tree(self):
		left_child = Node(2, None, None)
		left = Node(1, None, left_child)
		root = Node(3, left, Node(4, None, None))
		t = Tree(root)
		self.assertEqual(t.root.left.value, 1)
		self.assertEqual(t.root.left.right.value, 2)
		self.assertEqual(t.desc_ordered(), [4, 3, 2, 1])

	def test_can_print_empty_tree(self):
		t = Tree(None)
		self.assertEqual(t.desc_ordered(), [])

	def test_can_insert_and_delete_from_tree(self):
		to_add = list(range(100))
		random.shuffle(to_add)

		to_delete = [1, 18, 52, 93, 99]
		random.shuffle(to_delete)

		t = Tree(None)
		for v in to_add:
			t.insert(v)
			self.assertEqual(t.find(v), v)

		for v in to_delete:
			deleted = t.delete(v)
			# TO DO - add test to delete non-existant value
			self.assertEqual(deleted, True)
			self.assertEqual(t.find(v), None)

		expected = [v for v in to_add if v not in to_delete]
		expected.sort()
		expected.reverse()
		self.assertEqual(t.desc_ordered(), expected)

	def test_can_insert_to_tree(self):
		expected = list(range(100))
		random.shuffle(expected)

		t = Tree(None)
		for v in expected:
			t.insert(v)
			self.assertEqual(t.find(v), v)

		expected.sort()
		expected.reverse()
		self.assertEqual(t.desc_ordered(), expected)


if __name__ == '__main__':
    unittest.main()
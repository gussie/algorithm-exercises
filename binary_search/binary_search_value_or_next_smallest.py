'''
Implement a binary search function that, when given a search 
value and a sorted array, returns: 
- if the search value exists in the array, return the search value
- else: return the greatest value smaller than the search value 
- else: None

'''


import unittest, random


def binary_search(array, search_value, low, high):
	mid = int((low + high) / 2)
	
	if array[mid] == search_value: 
		return array[mid]

	if low == high:
		if search_value > array[high]: 
			return array[high]
		else:
			return array[high - 1]

	if search_value > array[mid]: 
		return binary_search(array, search_value, mid+1, high)
	else:
		return binary_search(array, search_value, low, mid-1)


def return_search_value(array, search_value): 
	if len(array) == 0:  #empty array
		return None

	low = 0
	high = len(array) - 1

	if search_value < array[low]: 
		return None
	else: 
		return binary_search(array, search_value, low, high)


class TestSearch(unittest.TestCase):

	def test_empty_list_returns_none(self):
		self.assertEqual(return_search_value([], 9), None)


	def test_can_find_search_value(self):
		self.assertEqual(return_search_value([1], 1), 1)
		self.assertEqual(return_search_value([1, 2], 1), 1)
		self.assertEqual(return_search_value([1, 2, 3], 1), 1)
		self.assertEqual(return_search_value([1, 2, 3], 2), 2)
		self.assertEqual(return_search_value([1, 2, 3], 3), 3)


	def test_if_value_smaller_than_everylist_element_returns_none(self):
		self.assertEqual(return_search_value([2], 1), None)
		self.assertEqual(return_search_value([2, 3], 1), None)
		self.assertEqual(return_search_value([2, 3, 4], 1), None)


	def test_value_not_in_list_returns_next_smallest(self):
		self.assertEqual(return_search_value([1, 3, 5], 2), 1)
		self.assertEqual(return_search_value([1, 3, 5, 7], 6), 5) 
		self.assertEqual(return_search_value([1, 3, 5], 4), 3) 
		self.assertEqual(return_search_value([1, 3, 5], 6), 5)


if __name__ == '__main__':
    unittest.main()
'''
Implement a dictionary via a Hashmap with two methods: 
- put()
- get()

'''


import unittest

class HashMap:
	def __init__(self, size=10):
		self._size = size
		self.list = [[]] * self._size

	def _hash(self, key):
		return key % self._size

	def put(self, key, value):
		element = self._hash(key)
		self.delete(key)
		self.list[element].append((key,value))

	def get(self, key):
		element = self._hash(key)
		for (k, v) in self.list[element]:
			if k == key: 
				return v
		return None

	def delete(self, key):
		element = self._hash(key)
		for (n, (k, v)) in enumerate(self.list[element]):
			if k == key: 
				self.list[element].pop(n)


class TestSearch(unittest.TestCase):
	def test_empty_map_returns_none(self):
		m = HashMap()
		self.assertEqual(m.get(1), None)

	def test_can_put_and_get_value(self):
		m = HashMap()
		m.put(1, "one")
		self.assertEqual(m.get(1), "one")

	def test_can_put_and_get_value_without_conflict(self):
		m = HashMap()
		m.put(1, "one")
		self.assertEqual(m.get(11), None)

	def test_can_put_and_get_two_values_with_same_hash(self):
		m = HashMap()
		m.put(1, "one")
		m.put(11, "eleven")
		self.assertEqual(m.get(1), "one")
		self.assertEqual(m.get(11), "eleven")

	def test_can_put_and_get_two_values_then_delete_one(self):
		m = HashMap()
		m.put(1, "one")
		m.put(11, "eleven")
		m.delete(11)
		self.assertEqual(m.get(1), "one")
		self.assertEqual(m.get(11), None)
		m.delete(1)
		self.assertEqual(m.get(1), None)

	def test_can_update_value(self):
		m = HashMap()
		m.put(1, "one")
		self.assertEqual(m.get(1), "one")
		m.put(1, "ONE")
		self.assertEqual(m.get(1), "ONE")

	def test_one_element_map_works(self):
		m = HashMap(size=1)
		m.put(1, "one")
		m.put(2, "two")
		m.put(3, "three")
		self.assertEqual(m.get(1), "one")
		self.assertEqual(m.get(2), "two")
		self.assertEqual(m.get(3), "three")

	def test_very_large_map_works(self):
		m = HashMap(size=100000)
		m.put(1, "one")
		m.put(2, "two")
		m.put(3, "three")
		self.assertEqual(m.get(1), "one")
		self.assertEqual(m.get(2), "two")
		self.assertEqual(m.get(3), "three")

if __name__ == '__main__':
    unittest.main()
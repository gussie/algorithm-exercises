# To run: python delete_random_dict_kv_pair.py

import unittest, random


class Dictionary: 

	def __init__(self):
		self.dict = {} # creating "delegate" dictionary
		self.list = []


	def put(self, key, value):
		if key not in self.dict: 		
			self.list.append(key)
		self.dict[key] = value


	def get(self, key):
		return self.dict[key]


	def __len__(self):
		return len(self.list)


	def delete(self):
		if len(self.list) == 0: 
			return None

		rand_index = random.randint(0, len(self.list)-1)
		if rand_index == len(self.list)-1:
			return self.list.pop()
		else:
			key_to_delete = self.list[rand_index]
			final_index = len(self.list)-1
			self.list[rand_index] = self.list[final_index]
			self.list[final_index] = key_to_delete
			del self.dict[key_to_delete]
			return self.list.pop()
		


class TestList(unittest.TestCase):

	def test_add_new_key_value_pair(self):
		d = Dictionary()
		self.assertEqual(len(d), 0)
		d.put('Caitlin', 36)
		self.assertEqual(len(d), 1)
		self.assertEqual(d.get('Caitlin'), 36)


	def test_delete__single_key(self):
		d = Dictionary()
		d.put('Caitlin', 36)
		self.assertEqual(d.delete(), 'Caitlin')


	def test_delete__empty_dict(self):
		d = Dictionary()
		self.assertEqual(d.delete(), None)


	def test_delete__can_delete_from_singleton_dict_with_multiple_puts(self):
		d = Dictionary()

		d.put('Caitlin', 36)
		self.assertEqual(d.get('Caitlin'), 36)
		d.put('Caitlin', 37)
		self.assertEqual(d.get('Caitlin'), 37)

		self.assertEqual(d.delete(), 'Caitlin')
		self.assertEqual(d.delete(), None)


	def test_add_and_delete__multiple_keys(self):
		d = Dictionary()
		d.put('Caitlin', 36)
		d.put('Rob', 37)
		d.put('Frida', 0)

		deleted_keys = []
		deleted_keys.append(d.delete())
		deleted_keys.append(d.delete())
		deleted_keys.append(d.delete())

		self.assertEqual(set(deleted_keys), set(['Caitlin', 'Frida', 'Rob']))

		

if __name__ == '__main__':
    unittest.main()
# To run: python delete_random_dict_kv_pair.py

import unittest


class Dictionary: 

	# def __init__(self, key, value):
	# 	self[key] = value

	def get_value(self, key):
		return self.key, self.value


	def put(self, value, list):
		# adds new key/value pair to dict
		self.key = key
		self.value = value
		print("Key: %s, value: %s pair" % (self.key, self.value))


	def delete_random(self):
		# put all dict keys into a list
		# generate r: random number between 0 and len(list)
		# swap list[r] & list[len]
			# key_to_delete = list[len]
			# delete
			# list.pop()
		# print("deleted key, value")
		pass


class TestList(unittest.TestCase):

	def test_add_new_key_value_pair(self):
		test_list = []
		caitlin = Dictionary.put("Elizabeth", test_list)
		robsie = Dictionary.put("Dion", test_list)
		frida = Dictionary.put("Marie", test_list)
		print(test_list)
		self.assertEqual(test_list.size(), 3)
		self.assertTrue(test_list.is_empty())
	

if __name__ == '__main__':
    unittest.main()
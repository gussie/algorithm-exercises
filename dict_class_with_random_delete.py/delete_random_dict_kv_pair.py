# To run: python delete_random_dict_kv_pair.py

import unittest


class Dictionary: 

	def __init__(self, key, value, list_of_keys):
		# adds new key/value pair to dict; and append key to list of keys
		self.key = key
		self.value = value
		list_of_keys.append(key)
		# print("Key: %s, Value: %s" % (self.key, self.value))


	def get_values(self, key):
		return self.key, self.value


	def delete_random(self, list_of_keys):
		rand_index = 1  #placeholder - TO DO: generate randNum(0, len(list_of_keys))
		key_to_delete = list_of_keys[rand_index]
		final_index = len(list_of_keys)-1
		list_of_keys[rand_index] = list_of_keys[final_index]
		list_of_keys[final_index] = key_to_delete
		list_of_keys.pop()
		
		self.key = None
		self.value = None
		# TO DO - delete the dictionary entry

		return list_of_keys, key_to_delete



class TestList(unittest.TestCase):

	# def test_add_new_key_value_pair(self):
	# 	test_list = []
	# 	caitlin = Dictionary('Caitlin', 'Elizabeth', test_list)
	# 	robsie = Dictionary('Robsie', 'Dion', test_list)
	# 	frida = Dictionary('Frida', 'Marie', test_list)
	# 	# self.assertEqual(Dictionary.get_values(), ['Caitlin', 'Robsie', 'Frida'])
	# 	self.assertEqual(len(test_list), 3)

	
	def test_remove_random_key_value_pair(self):
		test_list = []
		caitlin = Dictionary('Caitlin', 'Elizabeth', test_list)
		robsie = Dictionary('Robsie', 'Dion', test_list)
		frida = Dictionary('Frida', 'Marie', test_list)
		Dictionary.delete_random(self, test_list)

		

if __name__ == '__main__':
    unittest.main()
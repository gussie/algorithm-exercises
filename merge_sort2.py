

import unittest, random


def merge(left, right):
  # takes two sorted lists and returns one single sorted list
  l = 0 #initialize pointers for left and right lists
  r = 0 
  merged_array = []

  while l < len(left) or r < len(right):
    if l == len(left): 
      merged_array.append(right[r])
      r += 1
    elif r == len(right):
      merged_array.append(left[l])
      l += 1
    elif left[l] <= right[r]:
      merged_array.append(left[l])
      l += 1
    else: 
      merged_array.append(right[r])
      r += 1

  return merged_array


def mergesort(input_array):
  # returns an array in sorted order
  if len(input_array) <= 1: 
    return input_array

  middle = len(input_array) // 2
  left = input_array[:middle]
  right = input_array[middle:]

  sorted_left = mergesort(left)
  sorted_right = mergesort(right)

  sorted_array = merge(sorted_left, sorted_right)

  return sorted_array
  

class TestMergeSort(unittest.TestCase):

  def test_empty_list(self):
    expected_array = []
    self.assertEqual(expected_array, mergesort([]))


  def test_sorting(self):
    input = 'caitlin'
    expected_array = ['a', 'c', 'i', 'i', 'l', 'n', 't']
    self.assertEqual(expected_array, mergesort([*input]))


  def test_sorting_numbers(self):
    num = 1000
    inputs = [i+10 for i in range(num)]
    random.shuffle(inputs)

    outputs = [i+10 for i in range(num)]
    self.assertEqual(outputs, mergesort(inputs))
    

  def test_sort_already_sorted_list(self):
    num = 1000
    inputs = [i+10 for i in range(num)]

    outputs = [i+10 for i in range(num)]
    self.assertEqual(outputs, mergesort(inputs))


if __name__ == '__main__':
    unittest.main()
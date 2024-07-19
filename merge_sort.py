

import unittest, random

def merge(left, right):
  # takes two sorted arrays and returns one single array in sorted order
  l = 0
  r = 0
  sorted_array = []

  while (l < len(left)) or (r < len(right)):
    if r == len(right):
      sorted_array.append(left[l])
      l += 1
    elif l == len(left):
      sorted_array.append(right[r])
      r += 1
    elif (left[l] <= right[r]):
      sorted_array.append(left[l])
      l += 1
    else: 
      sorted_array.append(right[r])
      r += 1
  return sorted_array


def mergesort(array):
  # returns a sorted array
  if len(array) <= 1: 
    return array

  middle = len(array) // 2
  left = array[:middle]
  right = array[middle:]

  sorted_left = mergesort(left)
  sorted_right = mergesort(right)

  return merge(sorted_left, sorted_right)
  

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
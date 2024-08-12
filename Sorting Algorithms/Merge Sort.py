import random


def merge(list1 : list[int], list2 : list[int]) -> list[int]:
  combined : list[int] = []
  i = j = 0

  while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
      combined.append(list1[i])
      i += 1

    else:
      combined.append(list2[j])
      j += 1
  
  while i < len(list1):
    combined.append(list1[i])
    i += 1
  
  while j < len(list2):
    combined.append(list2[j])
    j += 1

  return combined


def merge_sort(my_list : list[int]) -> list[int]:
  if len(my_list) <= 1:
    return my_list

  mid_index : int = len(my_list)//2
  left : list[int] = merge_sort(my_list[:mid_index])
  right : list[int] = merge_sort(my_list[mid_index:])
  
  return merge(left, right)


def test_merge_sort() -> None:
  """Test cases for merge sort"""

  # Test case 1: Empty list
  assert merge_sort([]) == [], "Test case 1 failed"

  # Test case 2: Single element list
  assert merge_sort([5]) == [5], "Test case 2 failed"

  # Test case 3: Sorted list
  assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"

  # Test Case 4: Reverse sorted list
  assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 4 failed"

  # Test case 5: Random list
  assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9], "Test case 5 failed"

  # Test case 6: List with duplicates
  assert merge_sort([1, 2, 3, 3, 2, 1]) == [1, 1, 2, 2, 3, 3], "Test case 6 failed"

  # test case 7: Large list
  large_list = list(range(10000))
  random.shuffle(large_list)
  assert merge_sort(large_list) == list(range(10000)), "Test case 7 failed"
  
  print("All test cases passed!")


def main() -> None:
  test_merge_sort()

if __name__ == "__main__" :
  main()
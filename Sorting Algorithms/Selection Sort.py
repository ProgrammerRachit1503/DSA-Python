def selection_sort(my_list : list[int]) -> list[int]:
  for i in range(len(my_list) - 1):
    min_index : int = i
    
    for j in range(i + 1, len(my_list)):
      if my_list[j] < my_list[min_index]:
        min_index = j
    
    if i != min_index:
      my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

  return my_list


def test_selection_sort() -> ModuleNotFoundError:
    # Test case 1: Empty list
    assert selection_sort([]) == [], "Test case 1 failed"

    # Test case 2: Single element list
    assert selection_sort([1]) == [1], "Test case 2 failed"

    # Test case 3: List already sorted
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"

    # Test case 4: List sorted in reverse order
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 4 failed"

    # Test case 5: List with duplicate elements
    assert selection_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4], "Test case 5 failed"

    # Test case 6: Random order list
    assert selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

    print("All test cases passed!")


def main() -> None:
  test_selection_sort()

if __name__ == "__main__" :
  main()
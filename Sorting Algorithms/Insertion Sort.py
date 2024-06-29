def insertion_sort(my_list : list[int]) -> list[int]:
  for i in range(1, len(my_list)):
    temp : int= my_list[i]
    j : int = i - 1

    while temp < my_list[j] and j > -1:
      my_list[j + 1] = my_list[j]
      my_list[j] = temp
      j -= 1

  return my_list


def test_insertion_sort() -> None:
    # Test case 1: Empty list
    assert insertion_sort([]) == [], "Test case 1 failed"

    # Test case 2: Single element list
    assert insertion_sort([1]) == [1], "Test case 2 failed"

    # Test case 3: List already sorted
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"

    # Test case 4: List sorted in reverse order
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 4 failed"

    # Test case 5: List with duplicate elements
    assert insertion_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4], "Test case 5 failed"

    # Test case 6: Random order list
    assert insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

    print("All test cases passed!")


def main() -> None:
  test_insertion_sort()

if __name__ == "__main__" :
  main()
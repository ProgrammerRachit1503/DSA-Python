def bubble_sort(my_list : list[int]) -> list[int]:
  
  for i in range(len(my_list) - 1, 0, -1):
    
    for j in range(i):
      
      if my_list[j] > my_list[j + 1]:
        my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
  
  return my_list


def test_bubble_sort() -> None:
    # Test case 1: Empty list
    assert bubble_sort([]) == [], "Test case 1 failed"

    # Test case 2: Single element list
    assert bubble_sort([1]) == [1], "Test case 2 failed"

    # Test case 3: List already sorted
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"

    # Test case 4: List sorted in reverse order
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 4 failed"

    # Test case 5: List with duplicate elements
    assert bubble_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4], "Test case 5 failed"

    # Test case 6: Random order list
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

    print("All test cases passed!")


def main() -> None:
  test_bubble_sort()

if __name__ == "__main__" :
  main()
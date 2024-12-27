def __swap__(my_list: list[int], idx1: int, idx2: int) -> None:
    my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]


def __pivot__(my_list: list[int], pivot_idx: int, end_index: int) -> int:
    swap_idx: int = pivot_idx

    for i in range(pivot_idx + 1, end_index + 1):
        if my_list[i] < my_list[pivot_idx]:
            swap_idx += 1
            __swap__(my_list, swap_idx, i)

    __swap__(my_list, pivot_idx, swap_idx)
    return swap_idx


def __quick_sort_helper__(my_list: list[int], left: int, right: int) -> list[int]:
    if left < right:
        pivot_idx: int = __pivot__(my_list, left, right)

        __quick_sort_helper__(my_list, left, pivot_idx - 1)
        __quick_sort_helper__(my_list, pivot_idx + 1, right)
    return my_list


def quick_sort(my_list):
    return __quick_sort_helper__(my_list, 0, len(my_list) - 1)


def test_quick_sort() -> None:
    # Test case 1: Empty list
    assert quick_sort([]) == [], "Test case 1 failed"

    # Test case 2: Single element list
    assert quick_sort([1]) == [1], "Test case 2 failed"

    # Test case 3: List already sorted
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"

    # Test case 4: List sorted in reverse order
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5], "Test case 4 failed"

    # Test case 5: List with duplicate elements
    assert quick_sort([4, 2, 2, 3, 1]) == [1, 2, 2, 3, 4], "Test case 5 failed"

    # Test case 6: Random order list
    testcase6 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    solution6 = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    assert quick_sort(testcase6) == solution6, "Test case 6 failed"

    print("All test cases passed!")


def main() -> None:
    test_quick_sort()


if __name__ == "__main__":
    main()

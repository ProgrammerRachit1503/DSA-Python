def __swap__(my_list : list[int], idx1 : int, idx2 : int) -> None:
  my_list[idx1], my_list[idx2] = my_list[idx2], my_list[idx1]

def __pivot__(my_list : list[int], pivot_idx : int, end_index : int) -> int:
  swap_idx : int = pivot_idx

  for i in range(pivot_idx+1, end_index+1):
    if my_list[i] < my_list[pivot_idx]:
      swap_idx += 1
      __swap__(my_list, swap_idx, i)

  __swap__(my_list, pivot_idx, swap_idx)
  return swap_idx

def __quick_sort_helper__(my_list : list[int], left : int, right : int) -> list[int]:
  if left < right:
    pivot_idx  : int = __pivot__(my_list, left, right)

    __quick_sort_helper__(my_list, left, pivot_idx-1)
    __quick_sort_helper__(my_list, pivot_idx+1, right)
  return my_list

def quick_sort(my_list):
  return __quick_sort_helper__(my_list, 0, len(my_list)-1)


def main() -> None:
  pass

if __name__ == "__main__" :
  main()
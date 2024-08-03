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
  if len(my_list) == 1:
    return my_list

  mid_index : int = len(my_list)//2
  left : list[int] = merge_sort(my_list[:mid_index])
  right : list[int] = merge_sort(my_list[mid_index:])
  
  return merge(left, right)


def main() -> None:
  pass

if __name__ == "__main__" :
  main()
def item_in_common(list1, list2) -> bool:
  my_dict = {}
  
  for i in list1:
    my_dict[i] = True
   
  for j in list2:
    if j in my_dict:
      return True
  return False

def main() -> None:
  list1 = [1,3,5]
  list2 = [2,4,5]

  print(item_in_common(list1, list2))

if __name__ == "__main__" :
  main()
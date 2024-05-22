def find_duplicates(nums : list[int]) -> list[int]:
  nums_dict : dict = {}
  duplicates : list[int] = []
  for num in nums:
    if num in nums_dict.keys() and num not in duplicates:
      duplicates.append(num)
    else:
      nums_dict[num] = True
  return duplicates


def main() -> None:
  print ( find_duplicates([1, 2, 3, 4, 5]) )
  print ( find_duplicates([1, 1, 2, 2, 3]) )
  print ( find_duplicates([1, 1, 1, 1, 1]) )
  print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
  print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
  print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
  print ( find_duplicates([]) )

if __name__ == "__main__" :
  main()
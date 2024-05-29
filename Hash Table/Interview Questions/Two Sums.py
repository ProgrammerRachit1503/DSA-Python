def two_sum(nums : list[int], target : int) -> list[int]:
  Map : dict[int : int] = {}

  for i in range(len(nums)):
    compliment : int = target - nums[i]

    if compliment in Map.keys():
      return [Map[compliment], i]
    
    Map[nums[i]] = i
  
  return []


def main() -> None:
  print(two_sum([5, 1, 7, 2, 9, 3], 10))  
  print(two_sum([4, 2, 11, 7, 6, 3], 9))  
  print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))  
  print(two_sum([1, 3, 5, 7, 9], 10))  
  print (two_sum([1, 2, 3, 4, 5], 10))
  print (two_sum([1, 2, 3, 4, 5], 7))
  print (two_sum([1, 2, 3, 4, 5], 3))
  print (two_sum([], 0))

if __name__ == "__main__" :
  main()

"""
  EXPECTED OUTPUT:
  ----------------
  [1, 4]
  [1, 3]
  [0, 3]
  [1, 3]
  []
  [2, 3]
  [0, 1]
  []

"""
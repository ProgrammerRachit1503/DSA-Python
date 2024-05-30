def subarray_sum(nums : list[int], target : int) -> list[int]:
  cur_sum : int = 0
  Map : dict[int : int] = {}

  for idx, num in enumerate(nums):
    cur_sum += num
    
    if cur_sum == target:
      return [0, idx]

    if (cur_sum - target) in Map.keys():
      return [Map[cur_sum - target] + 1, idx]
    
    Map[cur_sum] = idx
  
  return []


def main() -> None:
  nums = [1, 2, 3, 4, 5]
  target = 9
  print ( subarray_sum(nums, target) )

  nums = [-1, 2, 3, -4, 5]
  target = 0
  print ( subarray_sum(nums, target) )

  nums = [2, 3, 4, 5, 6]
  target = 3
  print ( subarray_sum(nums, target) )

  nums = []
  target = 0
  print ( subarray_sum(nums, target) )

if __name__ == "__main__" :
  main()


"""
  EXPECTED OUTPUT:
  ----------------
  [1, 3]
  [0, 3]
  [1, 1]
  []

"""
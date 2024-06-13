def find_pairs(arr1 : list[int], arr2 : list[int], target : int) -> list[tuple[int]]:

  set1 : set = set(arr1)
  answer = []

  for num in arr2:
    compliment : int = target - num

    if compliment in set1:
      answer.append((compliment, num))

  return answer


def main() -> None:
  arr1 = [1, 2, 3, 4, 5]
  arr2 = [2, 4, 6, 8, 10]
  target = 7

  pairs = find_pairs(arr1, arr2, target)
  print (pairs)

if __name__ == "__main__" :
  main()

"""
  EXPECTED OUTPUT:
  ------------------------
  [(5, 2), (3, 4), (1, 6)]
  ------------------------

"""
def group_anagrams(strings : list[str]) -> list[list[str]]:
  sorted_string_dict : dict[str : list[str]] = {}
  
  for string in strings:
    reversed_string = ''.join(sorted(string))
    
    if reversed_string in sorted_string_dict.keys():
      sorted_string_dict[reversed_string].append(string)
    else:
      sorted_string_dict[reversed_string] = [string]

  anagrams_list : list[list[str]] = []

  for key in sorted_string_dict.keys():
    anagrams_list.append(sorted_string_dict[key])

  return anagrams_list


def test_group_anagrams() -> None:
  print("1st set:")
  print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

  print("\n2nd set:")
  print(group_anagrams(["abc", "cba", "bac", "foo", "bar"]))

  print("\n3rd set:")
  print(group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]))
  
  print("\n4th set:")
  print(group_anagrams(["DEER", "REED", "EDER"]))



def main() -> None:
  test_group_anagrams()

if __name__ == "__main__" :
  main()


"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]
"""
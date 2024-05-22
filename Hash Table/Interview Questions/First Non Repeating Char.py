def first_non_repeating_char(string : str) -> str | None:
  str_dict : dict[str : int] = {}
  for char in string:
    str_dict[char] = str_dict.get(char, 0) + 1

  for char in string:
    if str_dict[char] == 1:
      return char
  return None


def main() -> None:
  print( first_non_repeating_char('leetcode') )
  print( first_non_repeating_char('hello') )
  print( first_non_repeating_char('aabbcc') )

if __name__ == "__main__" :
  main()
class Stack:
  def __init__(self):
    self.stack_list = []

  def print_stack(self):
    for i in range(len(self.stack_list)-1, -1, -1):
      print(self.stack_list[i])

  def is_empty(self):
    return len(self.stack_list) == 0

  def peek(self):
    if self.is_empty():
      return None
    else:
      return self.stack_list[-1]

  def size(self):
    return len(self.stack_list)

  def push(self, value):
    self.stack_list.append(value)

  def pop(self):
    if self.is_empty():
      return None
    else:
      return self.stack_list.pop()


def is_balanced_parentheses(value : str) -> bool:
  method_Stack : Stack = Stack()
  for i in value:
    if i == "(":
      method_Stack.push(i)
    elif i == ")":
      checker = method_Stack.pop()
      if checker is None:
        return False
   
  if method_Stack.is_empty():
    return True
  return False



def test_is_balanced_parentheses():
  test_pass : int = 0

  try:
    assert is_balanced_parentheses('((()))') == True
    print('Test case 1 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 1 failed')

  try:
    assert is_balanced_parentheses('()') == True
    print('Test case 2 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 2 failed')

  try:
    assert is_balanced_parentheses('(()())') == True
    print('Test case 3 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 3 failed')

  try:
    assert is_balanced_parentheses('(()') == False
    print('Test case 4 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 4 failed')

  try:
    assert is_balanced_parentheses('())') == False
    print('Test case 5 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 5 failed')

  try:
    assert is_balanced_parentheses(')(') == False
    print('Test case 6 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 6 failed')

  try:
    assert is_balanced_parentheses('') == True
    print('Test case 7 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 7 failed')

  try:
    assert is_balanced_parentheses('()()()()') == True
    print('Test case 8 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 8 failed')

  try:
    assert is_balanced_parentheses('(())(())') == True
    print('Test case 9 passed')
    test_pass += 1
  except AssertionError:
      print('Test case 9 failed')

  try:
    assert is_balanced_parentheses('(()()())') == True
    print('Test case 10 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 10 failed')

  try:
    assert is_balanced_parentheses('((())') == False
    print('Test case 11 passed')
    test_pass += 1
  except AssertionError:
    print('Test case 11 failed')

  print(f"Test passed {test_pass}/11")

def main() -> None:
  test_is_balanced_parentheses()

if __name__ == "__main__" :
  main()
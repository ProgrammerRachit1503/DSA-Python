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



def reverse_string(string : str) -> str:
  func_stack : Stack = Stack()
  answer : str = ''
  for i in string:
    func_stack.push(i)
  for _ in range(func_stack.size()):
    answer += func_stack.pop()
  return answer



def main() -> None:
  my_string = 'hello world'

  print (reverse_string(my_string))



"""
  EXPECTED OUTPUT:
  ----------------
  dlrow olleh

"""

if __name__ == "__main__" :
  main()
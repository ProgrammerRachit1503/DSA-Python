class Stack:
  def __init__(self) -> None:
    self.stack_list : list[any] = []

  def print_stack(self) -> None :
    print(f"+----Your Stack----+")
    
    for i in range(len(self.stack_list)-1, -1, -1):
      print(self.stack_list[i])
    
    print(f"+------------------+")

  def push(self, value : any) -> bool:
    return self.stack_list.append(value)
  
  def pop(self) -> any | None:
    if len(self.stack_list) == 0:
      return None
    
    return self.stack_list.pop()
  
  def is_empty(self) -> bool:
    if len(self.stack_list) == 0:
      return True
    return False
  
  def peek(self) -> any | None:
    if self.is_empty():
      return None
    return self.stack_list[-1]
  
  def size(self) -> int:
    return len(self.stack_list)
  
  def make_empty(self) -> None :
    self.stack_list = []

def main() -> None:
  pass

if __name__ == "__main__" :
  main()
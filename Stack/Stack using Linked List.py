class Node:
  def __init__(self, value : any) -> None:
    self.value = value
    self.next = None

class Stack:
  def __init__(self, value : any) -> None:
    new_node : Node = Node(value)
    self.top = new_node
    self.height = 1

  def print_stack(self) -> None:
    temp : Node = self.top
    
    while temp is not None:
      print(temp.value)
      temp = temp.next
  
  def push(self, value : any) -> bool:
    new_node : Node = Node(value)
    new_node.next, self.top = self.top, new_node
    self.height += 1
    return True
  
  def pop(self) -> Node | None:
    if self.height == 0:
      return None
    
    temp : Node = self.top
    self.top, temp.next = self.top.next, None
    self.height -= 1
    return temp
  
  def is_empty(self) -> bool:
    if self.height == 0:
      return True
    return False

  def peek(self) -> Node | None:
    if self.is_empty():
      return None
    
    return self.top

  
  def size(self) -> int:
    return self.height
  
  def make_empty(self) -> None :
    self.top = None
    self.height = 0

def main() -> None:
  pass

if __name__ == "__main__" :
  main()
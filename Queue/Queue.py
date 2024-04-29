class Node:
  def __init__(self, value : any) -> None:
    self.value = value
    self.next = None

class Queue:
  def __init__(self, value : any) -> None:
    new_node : Node = Node(value)
    self.first : Node = new_node
    self.last : Node = new_node
    self.length : int = 1

  def print_queue(self) -> None:
    temp : Node = self.first
    
    while temp is not None:
      print(temp.value)
      temp = temp.next
  
  def enqueue(self, value : any) -> bool:
    new_node : Node = Node(value)
    
    if self.first is None:
      self.first = new_node
      self.last = new_node
    
    else: 
      self.last.next = new_node
      self.last = new_node
    
    self.length += 1
    return True
  
  def dequeue(self) -> Node | None :
    if self.length == 0:
      return None
    
    temp : Node = self.first
    if self.length == 1:
      self.last = None
    
    else: 
      self.first = self.first.next
      temp.next = None
      self.length -= 1
    return temp

def main() -> None:
  my_queue = Queue(7)
  my_queue.print_queue()

if __name__ == "__main__" :
  main()
class Node:
  def __init__(self, value : any) -> None:
    self.value : any = value
    self.next : Node = None

class LinkedList:
  def __init__(self, value : any) -> None:
    new_node : Node = Node(value)
    self.head : Node = new_node
    self.tail : Node = new_node
    self.length : int = 1
  
  def print_list(self) -> None: #Prints list
    temp : Node = self.head
    while temp is not None:
      print(temp.value, end=" -> ")
      temp = temp.next
    print(None)

  def append(self, value : any) -> bool:  #Insert at end
    new_node : Node = Node(value)
    
    if self.head is None: #checks for empty list
      self.head = new_node
      self.tail = new_node
    else: 
      self.tail.next = new_node
      self.tail = new_node
    
    self.length += 1
    return True
  
  def pop(self) -> Node: #Delete at end
    if self.length == 0:
      return None
    temp : Node = self.head
    prev : Node = self.head
    while(temp.next):
      prev = temp
      temp = temp.next
    self.tail = prev
    self.tail.next = None
    self.length -= 1
    if self.length == 0:
      self.head = None
      self.tail = None
    return temp
  
  def prepend(self, value : any) -> bool: #Insert at begin
    new_node : Node = Node(value)
    new_node.next = self.head
    self.head = new_node
    if self.tail is None:
      self.tail = new_node
    self.length += 1
    return True
  
  def pop_first(self) -> Node:
      if self.length == 0:
        return None
      
      temp : Node = self.head
      self.head = self.head.next
      temp.next = None
      self.length -= 1
      if self.length == 0:
        self.tail = None
      return temp
  
  def get(self, index : int) -> Node:
    if index >= self.length or index < 0:
      return None
    temp : Node = self.head
    for _ in range(index):
      temp = temp.next
    return temp
  
  def set_value(self, index : int, value : any) -> bool:
    temp : Node = self.get(index)
    if temp:
      temp.value = value
      return True
    return False
  
  def insert(self, index: int, value : any) -> bool:
    if index > self.length or index < 0:
      return False
    if index == 0:
      return self.prepend(value)
    if index == self.length:
      return self.append(value)
    new_node : Node = Node(value)
    temp : Node = self.get(index - 1)
    new_node.next = temp.next
    temp.next = new_node
    self.length += 1
    return True
  
  def remove(self, index : int) -> Node:
    if index >= self.length or index < 0:
      return None
    if index == 0:
      return self.pop_first()
    if index == (self.length - 1):
      return self.pop()
    prev : Node = self.get(index - 1)
    temp : Node = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp

  def reverse(self) -> None:
    temp : Node = self.head
    self.head = self.tail
    self.tail = temp
    after : Node = temp.next
    before : Node = None
    for _ in range(self.length):
      after = temp.next
      temp.next = before
      before = temp
      temp = after

  def make_empty(self):
    self.head = None
    self.tail = None
    self.length = 0

    


def main() -> None:
  my_linked_list = LinkedList(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  my_linked_list.append(4)
  my_linked_list.append(5)
  my_linked_list.append(5)

  print( my_linked_list.find_middle_node().value )


if __name__ == "__main__":
  main()
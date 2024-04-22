class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
    

class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def print_list(self) -> None:
    temp : Node = self.head
    
    while temp.next is not None:
      print(temp.value, end = ' <-> ')
      temp = temp.next
    print(temp.value)
    # print(None)
      
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
    self.length += 1
    return True
  
  def reverse(self) -> bool:
    if self.length == 0:
      return False
    
    if self.length == 1:
      pass
    
    else : 
      temp : Node = self.head
      
      while temp is not None:
        temp.next, temp.prev = temp.prev, temp.next
        temp = temp.prev
      
      self.head, self.tail = self.tail, self.head
      return True
  

def main() -> None:
  my_doubly_linked_list = DoublyLinkedList(1)
  my_doubly_linked_list.append(2)
  my_doubly_linked_list.append(3)
  my_doubly_linked_list.append(4)
  my_doubly_linked_list.append(5)


  print('DLL before reverse():')
  my_doubly_linked_list.print_list()


  my_doubly_linked_list.reverse()


  print('\nDLL after reverse():')
  my_doubly_linked_list.print_list()

if __name__ == "__main__" :
  main()
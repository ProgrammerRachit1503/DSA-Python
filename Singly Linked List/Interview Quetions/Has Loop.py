class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
        
class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1
    return True

  def has_loop(self):
    fast = self.head
    slow = self.head
    while fast is not None and fast.next is not None:
      fast = fast.next.next
      slow = slow.next
      if fast == slow:
        return True
    return False
    
    
def main() -> None:
  my_linked_list_1 = LinkedList(1)
  my_linked_list_1.append(2)
  my_linked_list_1.append(3)
  my_linked_list_1.append(4)
  my_linked_list_1.tail.next = my_linked_list_1.head
  print(my_linked_list_1.has_loop() ) # Returns True




  my_linked_list_2 = LinkedList(1)
  my_linked_list_2.append(2)
  my_linked_list_2.append(3)
  my_linked_list_2.append(4)
  print(my_linked_list_2.has_loop() ) # Returns False


if __name__ == "__main__":
  main()

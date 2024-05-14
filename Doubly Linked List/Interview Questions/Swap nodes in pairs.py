import unittest

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None
        

class DoublyLinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.length = 1

  def __str__(self):
    output = []
    current_node = self.head
    while current_node is not None:
      output.append(str(current_node.value))
      current_node = current_node.next
    return" <-> ".join(output)

  def print_list(self):
    print(self)
      
  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
    else:
      temp = self.head
      while temp.next is not None:
        temp = temp.next
      temp.next = new_node
      new_node.prev = temp
    self.length += 1
    return True

  def swap_pairs(self) -> bool:
    dummy_node : Node = Node(0)
    dummy_node.next = self.head

    point : Node = dummy_node
    while point.next and point.next.next:

      swap1 : Node = point.next
      swap2 : Node = point.next.next

      swap1.next, swap2.next = swap2.next, swap1
      swap2.prev, swap1.prev = point, swap2

      point.next = swap2
      point = swap1
    
    self.head = dummy_node.next
    return True
  
  def make_list_empty(self):
    self.head = None
    self.length = 0
    





class TestDoublyLinkedList(unittest.TestCase):

  def test_swap_pairs_empty(self):
    my_list = DoublyLinkedList(0)
    my_list.make_list_empty()
    my_list.swap_pairs()
    self.assertEqual(str(my_list), "")  # Assert empty list remains empty

  def test_swap_pairs_single(self):
    my_list = DoublyLinkedList(1)
    my_list.swap_pairs()
    self.assertEqual(str(my_list), "1")  # Assert single node remains unchanged

  def test_swap_pairs_even_length(self):
    my_list = DoublyLinkedList(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    expected_list = "2 <-> 1 <-> 4 <-> 3"
    my_list.swap_pairs()
    self.assertEqual(str(my_list), expected_list)

  def test_swap_pairs_odd_length(self):
    my_list = DoublyLinkedList(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    expected_list = "2 <-> 1 <-> 4 <-> 3 <-> 5"
    my_list.swap_pairs()
    self.assertEqual(str(my_list), expected_list)

if __name__ == "__main__":
  unittest.main()
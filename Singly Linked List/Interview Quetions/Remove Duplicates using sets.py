class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


#  self.tail is not given
class LinkedList:
  def __init__(self, value):
      new_node = Node(value)
      self.head = new_node
      self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
    else:
      current = self.head
      while current.next is not None:
        current = current.next
      current.next = new_node
    self.length += 1
  
  def print_list(self):
    if self.head is None:
      print("empty list")
    else:
      temp : Node = self.head
      while temp is not None:
        print(temp.value, end=" -> ")
        temp = temp.next
      print(None)


  def remove_duplicates(self):
    values = set()
    prev = None
    current = self.head
    while current is not None:
      if current.value in values:
        prev.next = current.next
        self.length -= 1
      else:
        values.add(current.value)
        prev = current
      current = current.next

def test_remove_duplicates(linked_list, expected_values):
  print("Before: ", end="")
  linked_list.print_list()
  linked_list.remove_duplicates()
  print("After:  ", end="")
  linked_list.print_list()

  # Collect values from linked list after removal
  result_values = []
  node = linked_list.head
  while node:
    result_values.append(node.value)
    node = node.next

  # Determine if the test passes
  if result_values == expected_values:
    print("Test PASS\n")
  else:
    print("Test FAIL\n")


def main() -> None:
  # Test 1: List with no duplicates
  ll = LinkedList(1)
  ll.append(2)
  ll.append(3)
  test_remove_duplicates(ll, [1, 2, 3])

  # Test 2: List with some duplicates
  ll = LinkedList(1)
  ll.append(2)
  ll.append(1)
  ll.append(3)
  ll.append(2)
  test_remove_duplicates(ll, [1, 2, 3])

  # Test 3: List with all duplicates
  ll = LinkedList(1)
  ll.append(1)
  ll.append(1)
  test_remove_duplicates(ll, [1])

  # Test 4: List with consecutive duplicates
  ll = LinkedList(1)
  ll.append(1)
  ll.append(2)
  ll.append(2)
  ll.append(3)
  test_remove_duplicates(ll, [1, 2, 3])

  # Test 5: List with non-consecutive duplicates
  ll = LinkedList(1)
  ll.append(2)
  ll.append(1)
  ll.append(3)
  ll.append(2)
  ll.append(4)
  test_remove_duplicates(ll, [1, 2, 3, 4])

  # Test 6: List with duplicates at the end
  ll = LinkedList(1)
  ll.append(2)
  ll.append(3)
  ll.append(3)
  test_remove_duplicates(ll, [1, 2, 3])

  # Test 7: Empty list
  ll = LinkedList(None)
  ll.head = None  # Directly setting the head to None
  ll.length = 0   # Adjusting the length to reflect an empty list
  test_remove_duplicates(ll, [])

if __name__ =="__main__":
  main()
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# self.tail is not given
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
    return True
  
  def print_list(self):
    temp = self.head
    while temp is not None:
      print(temp.value, end=" -> ")
      temp = temp.next
    print(None)   
          
  def make_empty(self):
    self.head = None
    self.length = 0

  def reverse_between(self, start_index, end_index):
    if self.length <= 1:
      return None
    
    dummy = Node(0)
    dummy.next = self.head
    prev_node = dummy
    
    for _ in range(start_index):
      prev_node = prev_node.next
    current = prev_node.next
    
    for _ in range(end_index - start_index):
      node_to_move = current.next
      current.next = node_to_move.next
      node_to_move.next = prev_node.next
      prev_node.next = node_to_move
    
    self.head = dummy.next

def main() -> None:
  linked_list = LinkedList(1)
  linked_list.append(2)
  linked_list.append(3)
  linked_list.append(4)
  linked_list.append(5)

  print("Original linked list: ")
  linked_list.print_list()

  # Reverse a sublist within the linked list
  linked_list.reverse_between(2, 4)
  print("Reversed sublist (2, 4): ")
  linked_list.print_list()

  # Reverse another sublist within the linked list
  linked_list.reverse_between(0, 4)
  print("Reversed entire linked list: ")
  linked_list.print_list()

  # Reverse a sublist of length 1 within the linked list
  linked_list.reverse_between(3, 3)
  print("Reversed sublist of length 1 (3, 3): ")
  linked_list.print_list()

  # Reverse an empty linked list
  empty_list = LinkedList(0)
  empty_list.make_empty
  empty_list.reverse_between(0, 0)
  print("Reversed empty linked list: ")
  empty_list.print_list()

if __name__ == "__main__":
  main()
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
        
# self.length is not given
class LinkedList:
  def __init__(self, value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node

      
  def append(self, value):
    new_node = Node(value)
    if self.head == None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    return True
      

  def find_middle_node(self):
    fast = self.head
    slow = self.head
    while fast is not None and fast.next is not None:
      fast = fast.next.next
      slow = slow.next
    return slow
  

def main() -> None:
  my_linked_list1 = LinkedList(1)
  my_linked_list1.append(2)
  my_linked_list1.append(3)
  my_linked_list1.append(4)
  my_linked_list1.append(5)

  print(my_linked_list1.find_middle_node().value)  #output => 3 
  
  my_linked_list2 = LinkedList(1)
  my_linked_list2.append(2)
  my_linked_list2.append(3)
  my_linked_list2.append(4)
  my_linked_list2.append(5)
  my_linked_list2.append(6)

  print(my_linked_list2.find_middle_node().value)  #output => 4 

if __name__ == "__main__":
  main()
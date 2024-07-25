class Node:
  def __init__(self, value : any = None, next = None) -> None:
    self.value : any = value
    self.next : Node = next

class LinkedList:
  def __init__(self, value : any = None) -> None:
    if value:
      new_node : Node = Node(value)
    self.head : Node = new_node if value else None
    self.tail : Node = new_node if value else None
    self.length : int = 1 if value else 0
  
  def print_list(self) -> None:
    temp : Node = self.head
    
    while temp is not None:
      print(temp.value, end=" -> ")
      temp = temp.next
    
    print(None)

  def append(self, value : any) -> bool:
    new_node : Node = Node(value)
    
    if self.head is None:
      self.head = new_node
      self.tail = new_node

    else: 
      self.tail.next = new_node
      self.tail = new_node

    self.length += 1
    return True

  def pop(self) -> Node:
    if self.length == 0:
      return None

    temp : Node = self.head
    prev : Node = self.head

    if self.length == 1:
      self.head = None
      self.tail = None

    else:
      while(temp.next):
        prev = temp
        temp = temp.next

      self.tail = prev
      self.tail.next = None

    self.length -= 1
    return temp

  def prepend(self, value : any) -> bool:
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
    if self.length == 1:
      self.tail = None

    else: 
      self.head = self.head.next
      temp.next = None
      self.length -= 1
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

  def make_empty(self) -> None:
    self.head = None
    self.tail = None
    self.length = 0

  # My code for bubble sort.
  def bubble_sort(self) -> None:
    if self.length <= 1:
      return    
    for i in range(self.length - 1, 0, -1):
      current = self.head

      for _ in range(i):
        if current.next and current.value > current.next.value:
          current.value, current.next.value = current.next.value, current.value

        current = current.next
  
  """
  Code of bubble sort provided by teacher on udemy and this is better approach but added as comment because this is not my solution.:-

  def bubble_sort(self) -> None:
    if self.length <= 1:
      return

    sorted_until : Node = None

    while sorted_until != self.head.next:
      current : Node = self.head

      while current.next != sorted_until:
        next_node : Node = current.next

        if current.value > next_node.value:
          current.value, next_node.value = next_node.value, current.value
        current = current.next

      sorted_until = current  
  """

  def selection_sort(self) -> None:
    if self.length <= 1:
      return
    
    selected : Node = self.head
    
    while selected.next is not None:

      temp : Node = selected.next
      min_value : Node = selected

      while temp is not None:
        if min_value.value > temp.value:
          min_value = temp
        temp = temp.next
      
      if selected != min_value:
        selected.value, min_value.value = min_value.value, selected.value
      selected = selected.next

  def insertion_sort(self) -> None:
    if self.length <= 1:
      return

    dummy_node = Node(next = self.head)
    prev, cur = self.head, self.head.next

    while cur:
      if cur.value >= prev.value:
        prev, cur = cur, cur.next
        continue

      temp = dummy_node

      while cur.value > temp.next.value:
        temp = temp.next

      prev.next = cur.next
      cur.next = temp.next
      temp.next = cur

      if prev.next is None:
        self.tail = cur
      cur = prev.next

    self.head = dummy_node.next


def create_linked_list(values):
  ll = LinkedList()
  for value in values:
    ll.append(value)
  return ll

# Helper function to convert linked list to Python list for easy comparison
def linked_list_to_list(ll):
  result = []
  current = ll.head
  while current:
    result.append(current.value)
    current = current.next
  return result


def test_bubble_sort():
  # Test case 1: Empty list
  ll1 = create_linked_list([])
  ll1.bubble_sort()
  assert linked_list_to_list(ll1) == [], "Test case 1 failed"

  # Test case 2: Single element list
  ll2 = create_linked_list([1])
  ll2.bubble_sort()
  assert linked_list_to_list(ll2) == [1], "Test case 2 failed"

  # Test case 3: List already sorted
  ll3 = create_linked_list([1, 2, 3, 4, 5])
  ll3.bubble_sort()
  assert linked_list_to_list(ll3) == [1, 2, 3, 4, 5], "Test case 3 failed"

  # Test case 4: List sorted in reverse order
  ll4 = create_linked_list([5, 4, 3, 2, 1])
  ll4.bubble_sort()
  assert linked_list_to_list(ll4) == [1, 2, 3, 4, 5], "Test case 4 failed"

  # Test case 5: List with duplicate elements
  ll5 = create_linked_list([4, 2, 2, 3, 1])
  ll5.bubble_sort()
  assert linked_list_to_list(ll5) == [1, 2, 2, 3, 4], "Test case 5 failed"

  # Test case 6: Random order list
  ll6 = create_linked_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
  ll6.bubble_sort()
  assert linked_list_to_list(ll6) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

  print("All test cases passed!")


def test_selection_sort():
  # Test case 1: Empty list
  ll1 = create_linked_list([])
  ll1.selection_sort()
  assert linked_list_to_list(ll1) == [], "Test case 1 failed"

  # Test case 2: Single element list
  ll2 = create_linked_list([1])
  ll2.selection_sort()
  assert linked_list_to_list(ll2) == [1], "Test case 2 failed"

  # Test case 3: List already sorted
  ll3 = create_linked_list([1, 2, 3, 4, 5])
  ll3.selection_sort()
  assert linked_list_to_list(ll3) == [1, 2, 3, 4, 5], "Test case 3 failed"

  # Test case 4: List sorted in reverse order
  ll4 = create_linked_list([5, 4, 3, 2, 1])
  ll4.selection_sort()
  assert linked_list_to_list(ll4) == [1, 2, 3, 4, 5], "Test case 4 failed"

  # Test case 5: List with duplicate elements
  ll5 = create_linked_list([4, 2, 2, 3, 1])
  ll5.selection_sort()
  assert linked_list_to_list(ll5) == [1, 2, 2, 3, 4], "Test case 5 failed"

  # Test case 6: Random order list
  ll6 = create_linked_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
  ll6.selection_sort()
  assert linked_list_to_list(ll6) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

  print("All test cases passed!")


def test_insertion_sort():
  # Test case 1: Empty list
  ll1 = create_linked_list([])
  ll1.insertion_sort()
  assert linked_list_to_list(ll1) == [], "Test case 1 failed"

  # Test case 2: Single element list
  ll2 = create_linked_list([1])
  ll2.insertion_sort()
  assert linked_list_to_list(ll2) == [1], "Test case 2 failed"

  # Test case 3: List already sorted
  ll3 = create_linked_list([1, 2, 3, 4, 5])
  ll3.insertion_sort()
  assert linked_list_to_list(ll3) == [1, 2, 3, 4, 5], "Test case 3 failed"

  # Test case 4: List sorted in reverse order
  ll4 = create_linked_list([5, 4, 3, 2, 1])
  ll4.insertion_sort()
  assert linked_list_to_list(ll4) == [1, 2, 3, 4, 5], "Test case 4 failed"

  # Test case 5: List with duplicate elements
  ll5 = create_linked_list([4, 2, 2, 3, 1])
  ll5.insertion_sort()
  assert linked_list_to_list(ll5) == [1, 2, 2, 3, 4], "Test case 5 failed"

  # Test case 6: Random order list
  ll6 = create_linked_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
  ll6.insertion_sort()
  assert linked_list_to_list(ll6) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9], "Test case 6 failed"

  print("All test cases passed!")


def main() -> None:
  pass


if __name__ == "__main__":
  main()
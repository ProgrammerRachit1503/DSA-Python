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
    
  def print_list(self):
    if self.head is None:
      print("empty list")
    else:
      temp = self.head
      values = []
      while temp is not None:
        values.append(str(temp.value))
        temp = temp.next
      print(" -> ".join(values)) 

  def binary_to_decimal(self):
    temp = self.head
    answer = 0
    length = self.length - 1
    while temp is not None:
      answer += (temp.value*(2 ** length))
      # answer = answer*2 + current.value
      length -= 1
      temp = temp.next
    return answer

def main() -> None:
  # Test case 1: Binary number 110 = Decimal number 6
  linked_list = LinkedList(1)
  linked_list.append(1)
  linked_list.append(0)
  result = linked_list.binary_to_decimal()
  try:
    assert result == 6
    print("Test case 1 passed, returned: ", result)
  except AssertionError:
    print("Test case 1 failed, returned: ", result)

  # Test case 2: Binary number 1000 = Decimal number 8
  linked_list = LinkedList(1)
  linked_list.append(0)
  linked_list.append(0)
  linked_list.append(0)
  result = linked_list.binary_to_decimal()
  try:
    assert result == 8
    print("Test case 2 passed, returned: ", result)
  except AssertionError:
    print("Test case 2 failed, returned: ", result)

  # Test case 3: Binary number 0 = Decimal number 0
  linked_list = LinkedList(0)
  result = linked_list.binary_to_decimal()
  try:
    assert result == 0
    print("Test case 3 passed, returned: ", result)
  except AssertionError:
    print("Test case 3 failed, returned: ", result)

  # Test case 4: Binary number 1 = Decimal number 1
  linked_list = LinkedList(1)
  result = linked_list.binary_to_decimal()
  try:
    assert result == 1
    print("Test case 4 passed, returned: ", result)
  except AssertionError:
    print("Test case 4 failed, returned: ", result)

  # Test case 5: Binary number 1101 = Decimal number 13
  linked_list = LinkedList(1)
  linked_list.append(1)
  linked_list.append(0)
  linked_list.append(1)
  result = linked_list.binary_to_decimal()
  try:
    assert result == 13
    print("Test case 5 passed, returned: ", result)
  except AssertionError:
    print("Test case 5 failed, returned: ", result)

if __name__ == "__main__":
  main()
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
      

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    new_node = Node(value)
    if self.root is None:
      self.root = new_node
      return True
    temp = self.root
    while (True):
      if new_node.value == temp.value:
        return False
      
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        temp = temp.left
      
      else: 
          if temp.right is None:
            temp.right = new_node
            return True
          temp = temp.right
  
  def ith_smallest(self, i : int) -> int:   # Using Iterative Approach using Stack
    NumStack : list[Node] = []
    current : Node = self.root

    while current or NumStack:
      while current:
        NumStack.append(current)
        current = current.left

      current = NumStack.pop()
      i -= 1
      
      if i == 0:
        return current.value
      
      current = current.right


def test_ith_smallest() -> None:
  # Test case 1: Typical BST
  bst = BinarySearchTree()
  bst.insert(10)
  bst.insert(5)
  bst.insert(15)
  bst.insert(2)
  bst.insert(7)
  bst.insert(12)
  bst.insert(17)
  
  assert bst.ith_smallest(1) == 2, "Test case 1 failed"
  assert bst.ith_smallest(2) == 5, "Test case 1 failed"
  assert bst.ith_smallest(3) == 7, "Test case 1 failed"
  assert bst.ith_smallest(4) == 10, "Test case 1 failed"
  assert bst.ith_smallest(5) == 12, "Test case 1 failed"
  assert bst.ith_smallest(6) == 15, "Test case 1 failed"
  assert bst.ith_smallest(7) == 17, "Test case 1 failed"

  # Test case 2: BST with single node
  bst_single = BinarySearchTree()
  bst_single.insert(10)
  
  assert bst_single.ith_smallest(1) == 10, "Test case 2 failed"

  # Test case 3: Left skewed BST
  bst_left = BinarySearchTree()
  bst_left.insert(10)
  bst_left.insert(5)
  bst_left.insert(2)
  bst_left.insert(1)
  
  assert bst_left.ith_smallest(1) == 1, "Test case 3 failed"
  assert bst_left.ith_smallest(2) == 2, "Test case 3 failed"
  assert bst_left.ith_smallest(3) == 5, "Test case 3 failed"
  assert bst_left.ith_smallest(4) == 10, "Test case 3 failed"

  # Test case 4: Right skewed BST
  bst_right = BinarySearchTree()
  bst_right.insert(10)
  bst_right.insert(15)
  bst_right.insert(20)
  bst_right.insert(25)
  
  assert bst_right.ith_smallest(1) == 10, "Test case 4 failed"
  assert bst_right.ith_smallest(2) == 15, "Test case 4 failed"
  assert bst_right.ith_smallest(3) == 20, "Test case 4 failed"
  assert bst_right.ith_smallest(4) == 25, "Test case 4 failed"

  print("All test cases passed!")


def main() -> None:
  test_ith_smallest()

if __name__ == "__main__" :
  main()
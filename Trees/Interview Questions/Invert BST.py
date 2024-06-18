class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
      
class BinarySearchTree:
  def __init__(self):
    self.root = None
                
  def __r_insert(self, current_node, value):
    if current_node == None: 
      return Node(value)   
    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    elif value > current_node.value:  # Changed to elif to avoid comparing twice if equal
      current_node.right = self.__r_insert(current_node.right, value) 
    return current_node    

  def r_insert(self, value):
      if self.root == None: 
        self.root = Node(value)
      else:
        self.__r_insert(self.root, value)  

  def invert(self) -> Node:
    return self.__invert_tree(self.root)

  def __invert_tree(self, root : Node) -> Node:
      
    if root :
        
      root.left, root.right = root.right, root.left
      
      self.__invert_tree(root.right)
      self.__invert_tree(root.left)
        
    return root


def tree_to_list(node):
  """Helper function to convert tree to list level-wise for easy comparison"""
  
  if not node:
    return []
  
  queue = [node]
  result = []
  
  while queue:
    current = queue.pop(0)
    if current:
      result.append(current.value)
      queue.append(current.left)
      queue.append(current.right)
    else:
      result.append(None)
  
  while result and result[-1] is None:  # Clean up trailing None values
    result.pop()
  
  return result

def test_invert_binary_search_tree():
  print("\n--- Testing Inversion of Binary Search Tree ---")
  
  scenarios = [
    ("Empty Tree", [], []),
    ("Single Node", [1], [1]),
    ("Tree with Left Child", [2, 1], [2, None, 1]),
    ("Tree with Right Child", [1, 2], [1, 2]),
    ("Multi-Level Tree", [3, 1, 5, 2], [3, 5, 1, None, None, 2]),
    ("Invert Twice", [4, 2, 6, 1, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
  ]

  for description, setup, expected in scenarios:
    bst = BinarySearchTree()
    
    for num in setup:
      bst.r_insert(num)
    
    if description == "Invert Twice":
      bst.invert()
    
    bst.invert()
    result = tree_to_list(bst.root)
    print(f"\n{description}: {'Pass' if result == expected else 'Fail'}")
    print(f"Expected: {expected}")
    print(f"Actual:   {result}")

def main() -> None:
  test_invert_binary_search_tree()

if __name__ == "__main__" :
  main()
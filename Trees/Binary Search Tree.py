class Node:
  def __init__(self, value: any) -> None:
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self) -> None:
    self.root = None

  def insert(self, value : any) -> bool:
    new_node : Node = Node(value)
    
    if self.root is None:
      self.root = new_node
      return True
    
    temp = self.root

    while True:
      if new_node.value == temp.value:
        return False
      
      if new_node.value < temp.value:
        if temp.left is None:
          temp.left = new_node
          return True
        
        temp : Node = temp.left
      
      else:
        if temp.right is None:
          temp.right = new_node
          return True
        
        temp = temp.right
  
  def contains(self, value) -> bool:
    temp : Node = self.root

    while temp is not None:
      if value < temp.value:
        temp = temp.left
      elif value > temp.value :
        temp = temp.right
      else:
        return True
    return False
  
  def __r_contains(self, current_node : Node, value : any) -> bool:
    if current_node == None:
      return False
    
    if value == current_node.value:
      return True
    
    if value < current_node.value:
      return self.__r_contains(current_node.left, value)
    
    if value > current_node.value:
      return self.__r_contains(current_node.right, value)
    
  def r_contains(self, value : any) -> bool:
    return self.__r_contains(self.root, value)

    

def main() -> None:
  pass

if __name__ == "__main__" :
  main()
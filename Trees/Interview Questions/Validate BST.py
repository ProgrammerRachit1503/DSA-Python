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
  
  def __r_insert(self, current_node : Node, value: any) -> Node | None:
    if current_node == None:
      return Node(value)

    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    
    if value > current_node.value:
      current_node.right = self.__r_insert(current_node.right, value)
    
    return current_node

  def r_insert(self, value : any) -> None:
    if self.root == None:
      self.root = Node(value)
    self.__r_insert(self.root, value)

  def __delete_node(self, current_node : Node, value : any) -> Node | None:
    if current_node == None:
      return None

    if value < current_node.value:
      current_node.left = self.__delete_node(current_node.left, value)

    elif value > current_node.value:
      current_node.right = self.__delete_node(current_node.right, value)
    
    else:
      if current_node.left == None and current_node.right == None:
        return None
      
      elif current_node.left == None:
        current_node = current_node.right
      
      elif current_node.right == None:
        current_node = current_node.left
      
      else:
        sub_tree_min : any = self.min_value(current_node.right)
        current_node.value = sub_tree_min
        current_node.right = self.__delete_node(current_node.right, sub_tree_min)

    return current_node

  def delete_node(self, value : any) -> None:
    self.__delete_node(self.root, value)

  def min_value(self, current_node : Node) -> any:
    while current_node.left is not None:
      current_node = current_node.left
    return current_node.value
  
  def DFS_in_order(self) -> list[int]:
    result : list[int] = []

    def traverse(current_node : Node):
      if current_node.left is not None:
        traverse(current_node.left)
      
      result.append(current_node.value)
      
      if current_node.right is not None:
        traverse(current_node.right)

    traverse(self.root)
    return result
  
  def is_bst_valid(self) -> bool:
    nums : list[int] = self.DFS_in_order()

    for idx in range(1, len(nums)):
      if nums[idx] <= nums[idx -1]:
        return False
    return True


def main() -> None:
  my_tree = BinarySearchTree()
  my_tree.insert(47)
  my_tree.insert(21)
  my_tree.insert(76)
  my_tree.insert(18)
  my_tree.insert(27)
  my_tree.insert(52)
  my_tree.insert(82)

  print(my_tree.is_bst_valid())

if __name__ == "__main__":
  main()
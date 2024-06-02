class MinHeap:
  def __init__(self) -> None:
    self.heap : list[int] = []

  def _left_child(self, index : int) -> int:
    return (index * 2) + 1 
  
  def _right_child(self, index : int) -> int:
    return (index + 1) * 2
  
  def _parent(self, index : int) -> int:
    return (index - 1) // 2
  
  def _swap(self, index1 : int, index2 : int) -> None:
    self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

  def insert(self, value : int) -> bool:
    self.heap.append(value)
    current : int = len(self.heap) - 1

    while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
      self._swap(current, self._parent(current))
      current = self._parent(current)

    return True
  
  def remove(self) -> int | None:
    if len(self.heap) == 0:
      return None
    
    if len(self.heap) == 1:
      return self.heap.pop()
    
    min_value : int = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)

    return min_value
  
  def _sink_down(self, index : int) -> None:
    min_index : int = index

    while True:
      left_index : int = self._left_child(index)
      right_index : int = self._right_child(index)

      if (left_index < len(self.heap) and self.heap[left_index] < self.heap[min_index]):
        min_index = left_index
      
      if right_index < len(self.heap) and self.heap[right_index] < self.heap[min_index]:
        min_index = right_index

      if min_index != index:
        self._swap(index, min_index)
        index = min_index
      else:
        return None


  def print_heap(self) -> None:
    print(self.heap)


def main() -> None:
  pass

if __name__ == "__main__" :
  main()
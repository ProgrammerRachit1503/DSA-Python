class MaxHeap:
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

    while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
      self._swap(current, self._parent(current))
      current = self._parent(current)

    return True
  
  def remove(self) -> int | None:
    if len(self.heap) == 0:
      return None
    
    if len(self.heap) == 1:
      return self.heap.pop()
    
    max_value : int = self.heap[0]
    self.heap[0] = self.heap.pop()
    self._sink_down(0)

    return max_value
  
  def _sink_down(self, index : int) -> None:
    max_index : int = index

    while True:
      left_index : int = self._left_child(index)
      right_index : int = self._right_child(index)

      if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
        max_index = left_index
      
      if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
        max_index = right_index

      if max_index != index:
        self._swap(index, max_index)
        index = max_index
      else:
        return None


  def print_heap(self) -> None:
    print(self.heap)


def find_kth_smallest(nums : list[int], k : int) -> int:
  Heap : MaxHeap = MaxHeap()
  
  for num in nums:
    Heap.insert(num)
    if len(Heap.heap) > k:
      Heap.remove()

  return Heap.remove()


def main() -> None:
  nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
  ks = [2, 3, 4, 7]
  expected_outputs = [2, 3, 4, 5]

  for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {"Yes" if result == expected_outputs[i] else "No"}')
    print('---------------------------------------')

if __name__ == "__main__" :
  main()
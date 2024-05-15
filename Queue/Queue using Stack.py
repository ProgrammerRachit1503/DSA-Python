class MyQueue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []

  def enqueue(self, value : any) -> bool:
    while len(self.stack1) > 0:
      self.stack2.append(self.stack1.pop())
    
    self.stack1.append(value)

    while len(self.stack2) > 0:
      self.stack1.append(self.stack2.pop())
    
    return True
    
  def dequeue(self):
    if self.is_empty():
      return None
    return self.stack1.pop()

  def peek(self):
    return self.stack1[-1]

  def is_empty(self):
    return len(self.stack1) == 0
        
        

def main() -> None:
  pass

if __name__ == "__main__" :
  main()
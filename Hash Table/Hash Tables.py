class HashTable:
  def __init__(self, size : int = 7) -> None:
    self.data_map = [None] * size

  def __hash(self, key : any) -> int:
    my_hash : int = 0

    for letter in key :
      my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
    
    return my_hash
  
  def print_table(self) -> None:
    for index, value in enumerate(self.data_map):
      print(f"{index} : {value}")

  def set_item(self, key : any, value: any) -> bool:
    index : int = self.__hash(key)
    
    if self.data_map[index] == None:
      self.data_map[index] = []
    
    self.data_map[index].append([key, value])
    return True
  
  def get_item(self, key : any) -> list:
    index : int = self.__hash(key)

    if self.data_map[index] is not None:
      for i in range(len(self.data_map[index])):
        if self.data_map[index][i][0] == key:
          return self.data_map[index][i][1]
    return None
  
  def keys(self) -> list:
    all_keys : list = []
    
    for i in range(len(self.data_map)):
      if self.data_map[i] is not None:
        for j in range(len(self.data_map[i])):
          all_keys.append(self.data_map[i][j][0])
    
    return all_keys


def main() -> None:
  pass

if __name__ == "__main__" :
  main()
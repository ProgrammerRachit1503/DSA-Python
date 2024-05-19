class Graph:
  def __init__(self) -> None:
    self.adj_list = {}

  def add_vertex(self, vertex) -> bool:
    if vertex not in self.adj_list.keys():
      self.adj_list[vertex] = [] 
      return True
    return False

  def add_edge(self, vertex_1, vertex_2) -> bool:
    if vertex_1 in self.adj_list.keys() and vertex_2 in self.adj_list.keys():
      self.adj_list[vertex_1].append(vertex_2)
      self.adj_list[vertex_2].append(vertex_1)
      return True
    return False 
  
  def remove_edge(self, vertex_1, vertex_2) -> bool:
    if vertex_1 in self.adj_list.keys() and vertex_2 in self.adj_list.keys():
      try:
        self.adj_list[vertex_1].remove(vertex_2)
        self.adj_list[vertex_2].remove(vertex_1)
      except ValueError:
        pass
      return True
    return False
  
  def remove_vertex(self, vertex):
    if vertex in self.adj_list.keys():
      for other_vertex in self.adj_list[vertex]:
        self.adj_list[other_vertex].remove(vertex)
      del self.adj_list[vertex]
      return True
    return False
  
  def print_graph(self) -> None:
    for i in self.adj_list:
      print(f"{i} : {self.adj_list[i]}")


def main() -> None:
  pass

if __name__ == "__main__" :
  main()
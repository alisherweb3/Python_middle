class Range2
  def __init__(self, stop_value: int):
    self.current = -1
    self.stop_value = stop_value -1
    
  def __iter__(self):
    return self
    
  def __next__(self):
    if self.current < self.stop_value:
      self.current += 1
      return self.current
    raise StopIteration
    
_range = Rnage(5)
for i in _range:
  print(i)
  
  

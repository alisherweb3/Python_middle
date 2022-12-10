class Range
  def __init__(self, stop_value: it):
    self.current = -1
    self.stop_value = stop_value -1
    
  def __iter__(self):
    return RangeIterator(self)
  
class RangeIterator:
  def __init__(self, container):
    self.container = container
    
  def __next__(self):
    if self.container.current < self.container.stop_value:
      self.container.current += 1
      return self.container.current
    raise StopIteration
    
_range = Rnage(5)
for i in _range:
  print(i)
  
  

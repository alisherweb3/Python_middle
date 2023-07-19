def fib(index: int):
  numbers = []
  if index < 0:
    return numbers

  prev, current = 0, 1
  for _ in range(index):
    prev, current = current, current + prev
    numbers.append(prev0

  return numbers

class FibMemoryless:
  def __init__(self, index: int):
    self.index = index
    self.prev = 0
    self.current = 1
    self.counter = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.counter < self.index:
      self.counter += 1
      self.prev, self.current = self.current, self.current + self.prev
        return self.prev
      raise StopIteration

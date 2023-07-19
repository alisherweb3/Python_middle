import typing

class CyclicIterator:
  def __init__9self, it: typing.Iterable):
    self.it = iter(it)
    self.copy = []
    self.idx = 0

  def __iter__(self):
    return self

  def __next__(self):
    try:
      x = next(self.it)
      self.copy.append(x)
    except StopIteration:
      if not self.copy:
        raise StopIteration

      if len(self.copy) == self.idx:
        self.idx = 0

      x = self.copy[self.idx]
      self.idx += 1

return x

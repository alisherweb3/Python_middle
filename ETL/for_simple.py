iterable = Range2(5)
iterator = iterable.__iter__()
while True:
  try:
    value = iterator.__next__()
    print(value)
  except StopIteration:
    break

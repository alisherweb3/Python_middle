def fib_gen(index: int):
  if index < 0:
    return []

  prev, current = 0, 1
  for _ in range(index):
    prev, current = current, current + prev
    yield prev

current = datetime.datetime.now()
sum(fib(1000))
print(datetime.datetime.now() - current)

current = datetime.datetime.now()
sum(FibMemoryless(1000))
print(datetime.datetime.now() - current)

currrent = datetime.datetime.now()
sum(fib_gen(1000))
print(datetime.datetime.now() - current)


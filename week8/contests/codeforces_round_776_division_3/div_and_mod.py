import math

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

  l, r, a = tuple([int(x) for x in input().split()])
  values = []

  # the rightmost value is the max
  values.append(r % a + math.floor(r/a))

  # the rightmost value has r%a=0 so we want to go one before that
  if r - 1 >= l:
    r2 = r - 1
    values.append(r2 % a + math.floor(r2/a))

  # go to the previous place where
  if r - r % a - 1 >= l:
    r3 = r - r % a - 1
    values.append(r3 % a + math.floor(r3/a))

  results.append(max(values))

for result in results:
  print(result)

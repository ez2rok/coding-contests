from math import floor

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

  x = int(input())
  n_serves = floor(x / 2 + 1)
  results.append(n_serves)

for result in results:
  print(result)

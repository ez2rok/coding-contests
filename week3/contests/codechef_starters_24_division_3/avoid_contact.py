n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
  n_total, n_sick = tuple([int(x) for x in input().split()])
  n_healthy = n_total - n_sick
  min_rooms = n_sick * 2 + n_healthy if n_healthy != 0 else n_sick * 2 - 1
  results.append(min_rooms)

for result in results:
  print(result)

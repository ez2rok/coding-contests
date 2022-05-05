n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
  a, b, c, x, y = tuple([int(x) for x in input().split()])  
  
  all_fed = max(x - a, 0) + max(y - b, 0) - c <= 0
  msg = 'yes' if all_fed else 'no'
  results.append(msg)
  
for result in results:
  print(result)

n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
 
  # get inputs
  x, y = tuple([int(x) for x in input().split()])
 
  # base case
  if x == 0 and y == 0:
    results.append(0)
    continue
  
  a = (x * x + y * y)**0.5 
  if a - int(a) == 0:
    results.append(1)
  else:
    results.append(2)
 
for result in results:
  print(result)

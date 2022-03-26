n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
 
  # get inputs
  n, B, x, y = tuple([int(x) for x in input().split()])
 
  sum_ = 0
  vals = [0]
  for _ in range(n):
    if sum_ + x > B:
      sum_ -= y
    else:
      sum_ += x
    vals.append(sum_)
 
  results.append(sum(vals))
 
for result in results:
  print(result)
  

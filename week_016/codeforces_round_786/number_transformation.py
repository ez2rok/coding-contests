n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
  x, y = tuple([int(x) for x in input().split()])
 
  # base cases
  if x > y:
    results.append([0, 0])
    continue
  if x == y:
    results.append([1, 1])
    continue
 
  found_solution = False
  for b in range(2, 101):
    val = x
    a = 0
    # print('b={}'.format(b))
    
    while val < y:
      val *= b
      a += 1
      # print('\ta={}\tval={}'.format(a, val))
 
    if val == y:
      found_solution = True
      break
 
  results.append([a, b] if found_solution else [0, 0])
  
for result in results:
  print(' '.join([str(x) for x in result]))
  

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
  # get inputs
  printer_1 = [int(x) for x in input().split()]
  printer_2 = [int(x) for x in input().split()]
  printer_3 = [int(x) for x in input().split()]
  
  # initial values
  result = []
  capacity = 1000000
  
  for p1, p2, p3 in zip(printer_1, printer_2, printer_3):
    val = min(p1, p2, p3)
    if result and sum(result) + val > capacity:
      val = capacity - sum(result)
    result.append(val)

  # record the answer
  result = 'IMPOSSIBLE' if sum(result) != capacity else ' '.join([str(x) for x in result])
  results.append(result)

print()
for i, result in enumerate(results):
  print('Case #{}: {}'.format(i+1, result))
   

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
  wind = input()
  vertical = 0
  horizontal = 0

  for x in wind:
    if x == 'L':
      horizontal -= 1
    elif x == 'R':
      horizontal += 1
    elif x == 'U':
      vertical += 1
    else:
      vertical -= 1

  msg = 'YES' if not vertical and not horizontal else 'NO'
  results.append(msg)
  
for result in results:
  print(result)
    

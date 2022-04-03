n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
  person = int(input())
  if person <= 18:
    results.append('Children')
  elif person <= 55:
    results.append('Citizens')
  else:
    results.append('Senior Citizens')
  
for result in results:
  print(result)
   

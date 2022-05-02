n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
  s = input()
  t = input()
 
  # base case
  if t == 'a':
    results.append(1)
    continue
 
  a_freq = t.count('a')
 
  # check for infinte number of different string combinations
  if a_freq >= 1:
    results.append(-1)
  elif len(s) == 1:
    results.append(2)
  else:
    results.append(pow(2, len(s)))
  
  
for result in results:
  print(result)

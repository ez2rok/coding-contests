n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
 
  n = int(input())
  A = [int(x) for x in input().split()]
 
  max_1 = max(A)
  A.remove(max_1)
  max_2 = max(A)
  results.append(max_1 + max_2)
 
for result in results:
  print(result)

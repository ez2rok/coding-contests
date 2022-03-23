import math

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n = int(input())
    a = math.floor(math.log2(n))
    
    val = sum([2**j - 1 for j in range(1, a)])
    val += n - 2 ** a 
    
    results.append(val)
    
for result in results:
    print(result)

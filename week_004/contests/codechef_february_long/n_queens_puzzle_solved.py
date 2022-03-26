from math import floor


n_test_cases = int(input())
results = []

def f(x):
   return (0.143 * x) ** x

for _ in range(n_test_cases):
    
    n_queens = int(input())
    x = f(n_queens)
    
    if x - floor(x) < 0.5:
        results.append(floor(x))
    else:
        results.append(floor(x) + 1)
        
for result in results:
    print(result)
    

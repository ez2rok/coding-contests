import math

# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_items = int(input())
    results.append(math.ceil(n_items / 10))
    
for result in results:
    print(result)

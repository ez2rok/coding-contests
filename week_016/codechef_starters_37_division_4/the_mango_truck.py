n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    x, y, z = tuple([int(x) for x in input().split()])
    
    results.append((z - y) // x)
    
for result in results:
    print(result)

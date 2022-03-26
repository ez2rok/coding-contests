n_test_cases= int(input())
results = []

for _ in range(n_test_cases):
    
    n = int(input())
    offset = 1 if n % 2 == 0 else -1
    results.append((n + 1) // 2 * offset)
    
for result in results:
    print(result)

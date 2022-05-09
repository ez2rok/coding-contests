n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    x, y = tuple([int(x) for x in input().split()])
    msg = 'Yes' if y <= x * 1.07 else 'No'
    results.append(msg)
    
for result in results:
    print(result)

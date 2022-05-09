n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    x, y = tuple([int(x) for x in input().split()])
    msg = 'Yes' if x == y and x > 0 else 'No'
    results.append(msg)
    
for result in results:
    print(result)
    

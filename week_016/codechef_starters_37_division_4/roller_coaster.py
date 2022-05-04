n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    x, h = tuple([int(x) for x in input().split()])
    msg = 'yes' if x >= h else 'no'
    results.append(msg)
    
for result in results:
    print(result)

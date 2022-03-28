n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    # get inputs
    x, y, a, b = tuple([int(x) for x in input().split()])
    
    # update count
    count = 2
    count -= x in [a, b]
    count -= y in [a, b]
    
    results.append(count)
    
for result in results:
    print(result)

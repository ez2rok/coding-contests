# cook your dish here

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_points = int(input())
    xs = []
    ys = []
    for _ in range(n_points):
        x, y = tuple([int(x) for x in input().split()])
        xs.append(x)
        ys.append(y)
        
    
    n_distinct_lines = len(set(xs)) + len(set(ys))
    results.append(n_distinct_lines)
    
for result in results:
    print(result)
    

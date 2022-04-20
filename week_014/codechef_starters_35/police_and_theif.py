# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    x, y = tuple([int(x) for x in input().split()])
    results.append(abs(x - y))
    
for result in results:
    print(result)

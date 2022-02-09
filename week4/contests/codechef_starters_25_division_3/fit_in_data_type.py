# cook your dish here

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    N, X = tuple([int(x) for x in input().split()])
    results.append(X % (N + 1))

for result in results:
    print(result)
    

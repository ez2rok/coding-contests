# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_bottles, liters_per_bottle, n_liters = tuple([int(x) for x in input().split()])
    results.append(min(n_bottles, n_liters // liters_per_bottle))
    
for result in results:
    print(result)

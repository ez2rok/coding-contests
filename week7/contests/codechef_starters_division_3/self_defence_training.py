# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_women = int(input())
    ages = [int(x) for x in input().split()]
    eligible = [10 <= age <= 60 for age in ages]
    results.append(sum(eligible))
    
for result in results:
    print(result)

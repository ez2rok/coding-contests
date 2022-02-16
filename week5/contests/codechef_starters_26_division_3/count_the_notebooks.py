# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    n_pulp = int(input())
    n_notebooks = n_pulp * 10
    results.append(n_notebooks)
    
for result in results:
    print(result)
    

# cook your dish here

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_bananas, n_apples = tuple([int(x) for x in input().split()])
    n_chaat = min(n_apples, n_bananas // 2)
    results.append(n_chaat)
    
for result in results:
    print(result)

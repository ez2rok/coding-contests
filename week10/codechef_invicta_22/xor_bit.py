# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    n, k = tuple([int(x) for x in input().split()])
    
    # base case 
    if k == 1:
        results.append(1 if n % 4 == 1 or n % 4 == 2 else 0)
        continue
    
    x = n % (2 ** k)
    if x < (2 ** (k - 1)):
        results.append(0)
    elif x % 2 == 0:
        results.append(1) 
    else:
        results.append(0)
        
for result in results:
    print(result)
        

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    # get inputs
    n = int(input())
    s = input()
    
    n_ones = sum([int(x) for x in s])
    n_zeros = len(s) - n_ones
    
    if abs(n_ones - n_zeros) <= 1:
        results.append(len(s))
    else:
        results.append(2*min(n_zeros, n_ones) + 1)
        
for result in results:
    print(result)

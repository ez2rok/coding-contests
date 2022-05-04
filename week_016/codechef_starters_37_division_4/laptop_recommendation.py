from collections import Counter

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n = int(input())
    A = [int(x) for x in input().split()]
    freq = [0] * 11
    
    for a in A:
        freq[a] += 1
        
    max_freq = max(freq)
    max_vals = [i for i, f in enumerate(freq) if f == max_freq]
    result = 'confused' if len(max_vals) > 1 else max_vals[0]
    results.append(result)
    
for result in results:
    print(result)
    

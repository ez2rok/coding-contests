from collections import Counter

# get inputs
A_len, B_len, C_len = [int(x) for x in input().split()]
A = [int(input()) for _ in range(A_len)]
B = [int(input()) for _ in range(B_len)]
C = [int(input()) for _ in range(C_len)]

def has_duplicates(freq):
    return freq > 1

ids = A + B + C
id_to_freq = Counter(ids)
results = sorted([id_ for id_, freq in id_to_freq.items() if has_duplicates(freq)])

print(len(results))
for result in results:
    print(result)
    

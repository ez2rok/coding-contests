from collections import Counter

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    # get inputs
    len_S = int(input())
    S = [int(x) for x in input().split()]

    # get frequencies and sort it
    val_to_freq = Counter(S)
    val_to_freq = dict(sorted(val_to_freq.items(), key= lambda x: x[0]))

    count = 0
    for val, freq in val_to_freq.items():
      while freq > 0 and count < val:
        count += 1
        freq -= 1
    results.append(count)

for i, result in enumerate(results):
  print('Case #{}: {}'.format(i+1, result))
    

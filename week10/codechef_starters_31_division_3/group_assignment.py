n_test_cases= int(input())
results = []

for _ in range(n_test_cases):
    mid, x = tuple([int(x) for x in input().split()])
    diff = abs(x - mid)

    if x > mid:
        results.append(mid - diff + 1)
    else:
        results.append(mid + diff + 1)
        
for result in results:
    print(result)

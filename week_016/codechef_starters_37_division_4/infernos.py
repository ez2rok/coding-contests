n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n, x = tuple([int(x) for x in input().split()])
    H = [int(x) for x in input().split()]
    
    multi_mode_time = max(H)
    single_mode_time = 0
    
    for h in H:
        single_mode_time += (h + x - 1) // x
        
    results.append(min(single_mode_time, multi_mode_time))
    
for result in results:
    print(result)
    

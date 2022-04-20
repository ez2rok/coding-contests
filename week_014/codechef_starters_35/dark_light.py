n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n, k = tuple([int(x) for x in input().split()])
        
    if k == 0: # flashlight is off
        results.append('Off' if n % 4 == 0 else 'On')
    elif n == 0: # flashlight is on but doesn't change state
        results.append('Off' if k == 0 else 'On')
    else: # flashlight is on and make 4x changes for some x
        results.append('On' if n % 4 == 0 else 'Ambiguous')
    
for result in results:
    print(result)

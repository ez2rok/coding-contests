# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    len_, initial_state = tuple([int(x) for x in input().split()])
    A = [int(x) for x in input().split()]
    A.insert(0, initial_state)

    local_max = [float('-inf')]
    for i, a in enumerate(A):
        local_max.append(max(0, local_max[i]) + a)
        
    max_ = max(local_max)
    results.append(max_)
    
for result in results:
  print(result)
       

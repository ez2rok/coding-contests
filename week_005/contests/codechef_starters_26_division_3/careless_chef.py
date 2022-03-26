# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    len_ = int(input())
    B = [int(x) for x in input().split()]
    
    n_even_numbers = sum([b % 2 == 0 for b in B])
    if n_even_numbers % 2 == 1: # if have an odd amount of even n_odd_numbers
        results.append('no')
    else:
        results.append('yes')
        
        
for result in results:
    print(result)
    

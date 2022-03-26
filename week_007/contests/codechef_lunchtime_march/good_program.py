# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_bits = int(input())
    results.append('Good' if n_bits % 4 == 0 else 'Not Good')
    
for result in results:
    print(result)

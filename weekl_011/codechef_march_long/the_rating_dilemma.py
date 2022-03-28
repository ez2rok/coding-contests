n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    ratings_sum = int(input())
    results.append(-1 * (abs(ratings_sum) + 1))
    
for result in results:
    print(result)
        

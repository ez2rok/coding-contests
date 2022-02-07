n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    n_people, minutes_per_person = tuple([int(x) for x in input().split()])
    wait_time = n_people * minutes_per_person
    results.append(wait_time)
    
for result in results:
    print(result)
    

# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    n_festivals = int(input())
    festivals = [int(x) for x in input().split()]
    weekends = [6, 7, 13, 14, 20, 21, 27, 28]
    days_off = festivals + weekends
    n_days_off = len(set(days_off))
    results.append(n_days_off)
    
for result in results:
    print(result)

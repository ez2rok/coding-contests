# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    fuel_economy_1, fuel_economy_2, gas_price_1, gas_price_2 = tuple([int(x) for x in input().split()])
    rupee_per_kilometer_1 = gas_price_1 / fuel_economy_1
    rupee_per_kilometer_2 = gas_price_2 / fuel_economy_2
    if rupee_per_kilometer_1 < rupee_per_kilometer_2:
        results.append(-1)
    elif rupee_per_kilometer_1 > rupee_per_kilometer_2:
        results.append(1)
    else:
        results.append(0)
        
for result in results:
    print(result)

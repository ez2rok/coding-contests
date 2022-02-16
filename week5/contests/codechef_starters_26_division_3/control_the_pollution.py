# cook your dish here
import math

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    n_people, pollution_per_bus, pollution_per_car = tuple([int(x) for x in input().split()])
    
    n_buses = math.ceil(n_people / 100)
    n_cars = math.ceil(n_people / 4)
    bus_pollution = n_buses * pollution_per_bus # pollution from only buses
    car_pollution = n_cars * pollution_per_car # pollution from only cars
    
    n_buses = math.floor(n_people / 100)
    n_cars = math.ceil((n_people % 100) / 4)
    mixed_pollution = n_buses * pollution_per_bus + n_cars * pollution_per_car # pollution from both buses, cars
    
    pollution = min(bus_pollution, car_pollution, mixed_pollution)
    results.append(pollution)
    
for result in results:
    print(result)
    

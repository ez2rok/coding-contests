import numpy as np

# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    # get inputs
    n_tasks = int(input())
    task_times = [int(x) for x in input().split()]
    
    # compute cumlative sum in O(n)
    cumlative_sum = [task_times[0]]
    [cumlative_sum.append(cumlative_sum[-1] + time) for time in task_times[1:]]
    
    # ideally, if x is the amount of time it takes to run all of the operations,
    # each processer will spend x/2 time doing operations
    total_time = sum(task_times)
    half_time = total_time / 2
    distance_from_half_time = [abs(sum_ - half_time) for sum_ in cumlative_sum]
    min_idx = np.argmin(distance_from_half_time)
    
    processer_1_time = cumlative_sum[min_idx]
    processer_2_time = total_time - cumlative_sum[min_idx]
    min_time = max(processer_1_time, processer_2_time)
    results.append(min_time)
    
for result in results:
    print(result)

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

    # get input
    x = [int(x) for x in list(input())]

    # compute values
    sum_ = sum(x)
    n_zeros = len(x) - sum_
    n_ones = sum_
    min_ = min(n_ones, n_zeros)

    if n_ones != n_zeros:
        results.append(min_)
    else: # if n_ones == n_zeros
        results.append(min_ - 1)

for result in results:
    print(result)

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

    # get input
    n = int(input().lstrip('0'))

    # compute the ones_digit and the remainder
    ones_digit = n % 10
    remainder = n % 7

    # edge case: the number already perfectly divides by 7
    if remainder == 0:
        results.append(n)
        continue

    # make a new number that is divisible by 7 by changing the one's digit
    n_new = n - remainder + 7 if ones_digit - remainder < 0 else n - remainder
    results.append(n_new)


for result in results:
    print(result)

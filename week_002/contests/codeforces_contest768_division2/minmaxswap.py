def min_max_swap(a, b):
    
    for i in range(len(a)):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]



n_test_cases = int(input())

for _ in range(n_test_cases):

    # pase inputs
    n = int(input())
    a = [int(x) for x in input().split(' ')]
    b = [int(x) for x in input().split(' ')]

    # call min_mx_swap where the first argument is the array
    # that contains the largest element from both a and b
    if max(a) > max(b):
        min_max_swap(a, b)
    else:
        min_max_swap(b, a)

    # print the minimum product of the max of two arrays
    print(max(a) * max(b))
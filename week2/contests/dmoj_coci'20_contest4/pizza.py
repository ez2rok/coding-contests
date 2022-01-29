# initial values
results = []
n_test_cases = int(input())

for _ in range(n_test_cases):

    a, b, c, d = map(int, input().split())

    product_1, product_2 = 1, 1
    for i in range(a, b + 1):
        product_1 *= i 
    for i in range(c, d + 1):
        product_2 *= i 

    if product_2 % product_1 == 0:
        results.append('DA')
    else:
        results.append('NE')

for result in results:
    print(result)

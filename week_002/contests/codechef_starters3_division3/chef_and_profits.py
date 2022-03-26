# cook your dish here
n_test_cases = int(input())

for _ in range(n_test_cases):
    n_stocks, price_bought, price_sold = tuple([int(x) for x  in input().split(' ')])
    profit = n_stocks * (price_sold - price_bought)
    print(profit)

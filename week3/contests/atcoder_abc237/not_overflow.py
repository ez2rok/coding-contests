x = int(input())
print('Yes') if x <= 2 ** 31 - 1 and x >= -2 ** 31 else print('No')

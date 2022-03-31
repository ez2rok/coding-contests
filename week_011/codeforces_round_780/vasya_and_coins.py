n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
 
  # get inputs
  one_coins, two_coins = tuple([int(x) for x in input().split()])
 
  if one_coins == 0:
    results.append(1)
  else: # have both one and two coins
    results.append(one_coins + 2 * two_coins + 1)
 
  
for result in results:
  print(result)

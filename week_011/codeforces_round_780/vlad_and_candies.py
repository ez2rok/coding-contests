n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
 
  # get inputs
  n_types_of_candies = int(input())
  candies = [int(x) for x in input().split()]
 
  # base case:
  if len(candies) == 1:
    msg = 'no' if candies[0] > 1 else 'yes'
    results.append(msg)
    continue
 
  # get the two greatest elements in candies
  max1 = max(candies)
  candies.remove(max1)
  max2 = max(candies)
 
  msg = 'no' if max1 - max2 > 1 else 'yes'
  results.append(msg)
  
for result in results:
  print(result)

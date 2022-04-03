from collections import Counter

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
  # get inputs
  r, c = tuple([int(x) for x in input().split()])

  # create result
  result = '..+{}\n'.format('-+' * (c-1))
  for i in range(r):
    if i == 0:
      result += '..{}|\n'.format('|.' * (c - 1))
    else:
      result += '{}|\n'.format('|.' * c)
    result += '+{}'.format('-+' * c)
    if i != r - 1:
      result += '\n'

  results.append(result)

for i, result in enumerate(results):
  print('Case #{}:\n{}'.format(i+1, result))
    

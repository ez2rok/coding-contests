from collections import defaultdict
import string

n_test_cases = int(input())
results = []

def get_repetitions_idx(molecule):
  for i, char in enumerate(molecule):
    if char in string.ascii_uppercase:
      return i

for _ in range(n_test_cases):

  # get and parse input
  equation = input()
  lhs, rhs = tuple(equation.split('->'))
  lhs, rhs = lhs.split('+'), rhs.split('+')

  molecule_to_freq = defaultdict(int)

  # LHS
  for molecule in lhs:
    
    idx = get_repetitions_idx(molecule)
    vals = [1 if idx == 0 else int(molecule[:idx])]
    for char in molecule[idx:]:        
      if char.isdigit():
        vals[-1] += char
      else:
        vals.append(char)

    repetition = vals[0]
    for x in vals[1:]:
      if len(x) == 1:
        molecule_to_freq[x] += repetition
      else:
        molecule_to_freq[x[0]] += repetition * int(x[1:])
  
  # RHS
  for molecule in rhs:
    
    idx = get_repetitions_idx(molecule)
    vals = [1 if idx == 0 else int(molecule[:idx])]
    for char in molecule[idx:]:        
      if char.isdigit():
        vals[-1] += char
      else:
        vals.append(char)

    repetition = vals[0]
    for x in vals[1:]:
      if len(x) == 1:
        molecule_to_freq[x] -= repetition
      else:
        molecule_to_freq[x[0]] -= repetition * int(x[1:])

  msg = 'DA'
  for x in molecule_to_freq.values():
    if x != 0:
      msg = 'NE'
      break
  
  results.append(msg)
  

for result in results:
  print(result)

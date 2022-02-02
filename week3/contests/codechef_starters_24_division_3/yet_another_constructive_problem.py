n_test_cases = int(input())
results = []

def test(result):
  A, B, C = tuple(result)
  return (A|B) & (B|C) & (C|A)

for _ in range(n_test_cases):

  A = 536870911 # 2^29 - 1, ie 28 bits of all ones
  B = 0 # 28 bits of all zeros
  C = int(input())
  results.append([A, B, C])

for result in results:
  [print(x, end=" ") for x in result]
  print()

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

  # get inputs
  s_length, n_operations = tuple([int(x) for x in input().split()])
  s = input()

  # determine if is palindrome
  is_palindrome = True
  l, r = 0, len(s) - 1
  while l < r:
    if s[l] != s[r]:
      is_palindrome = False
    l += 1
    r -= 1

  n_different_strings = 1 if n_operations == 0 or is_palindrome else 2

  results.append(n_different_strings)

for result in results:
  print(result)

n_test_cases = int(input())
results = []
 
for _ in range(n_test_cases):
  s = input()
  char1 = ord(s[0]) - ord('a')
  char2 = ord(s[1]) - ord('a')
 
  val = char1 * 25 + char2 + int(char2 < char1)
  results.append(val)
  
for result in results:
  print(result)

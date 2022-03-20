# get inputs
n = int(input())
A = list(range(1, 2*n+2))
 
while len(A) > 0:
 
  # I chose a number
  print(A.pop(), flush=True)
 
  if len(A) <= 0:
    break
 
  # opponent choses a number
  a = int(input())
  A.pop(A.index(a))

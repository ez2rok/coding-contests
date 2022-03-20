# get inputs
n = int(input())
A = input()
 
# direction
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
position = [0, 0]
 
 
def add(A, B):
  return [a+b for a, b in zip(A, B)]
 
count = 0
for a in A:
  if a == 'R':
    count += 1
  else:
    position = add(position, directions[count % 4])
 
print(position[0], position[1])

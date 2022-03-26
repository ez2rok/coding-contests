# get inputs
n, speed = [int(x) for x in input().split()]
terrain = [x for x in input()]

# get numerical values for the terrain sections
mapping = {'F': 0, 'D': 1, 'U': -1}
terrain = [mapping[x] for x in terrain]

# initial values
n_walks = 0

# loop through each section of terrain and determine if will need to walk there
for change in terrain:
    if speed + change <= 0:
        n_walks += 1
        speed = 0
    else:
        speed += change

print(n_walks)

# cook your dish here
manhattan_distance = int(input())
results = []

if manhattan_distance % 2 != 0:
    results.append(-1)
else:
    results = ['0 {}'.format(manhattan_distance // 2), 
               '{} 0'.format(manhattan_distance // 2), 
               '0 {}'.format(- manhattan_distance // 2),
               '{} 0'.format(-manhattan_distance // 2)]

for result in results:
    print(result)

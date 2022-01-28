N = int(input())
i = int(input())
j = int(input())

if abs(i * i - N) < abs(j * j - N): # i^2 is closer to N than j^2
    print(1)
else: # j^2 is closer to N than i^2
    print(2)

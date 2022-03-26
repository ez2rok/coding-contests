# get inputs
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# compute transpose
import numpy as np
B = np.array(A).T

# print transpose
for row in B:
    for b in row:
        print(b, end=' ')
    print()

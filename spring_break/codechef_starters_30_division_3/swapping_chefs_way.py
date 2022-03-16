# cook your dish here
n_test_cases = int(input())
results = []

def matches(i, A, A_sorted):
    j = len(A) - (i + 1)
    val1 = A[i] == A_sorted[i] and A[j] == A_sorted[j]
    val2 = A[i] == A_sorted[j] and A[j] == A_sorted[i]
    return val1 or val2

for _ in range(n_test_cases):
    
    A_len = int(input())
    A = input()
    A_sorted = sorted(A)
    
    val = 'YES'
    for i in range(A_len // 2):
        if not matches(i, A, A_sorted):
            val = 'NO'
            break
        
    results.append(val)
      
for result in results:
    print(result)

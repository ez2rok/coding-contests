# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    # get inputs
    n_ints = int(input())
    A = [int(x) for x in input().split()]
    polarity = input()
    
    # sort A
    A_sorted = sorted(A)
    
    # case 1: A is one element
    if len(A) == 1:
        results.append(0)
        continue
    
    # case 2: A is already sorted
    if A == A_sorted:
        results.append(0)
        continue
        
    # case 3: A is not sorted and consists of all N's or all S's, ie we cannot sort it
    if 'S' not in polarity or 'N' not in polarity:
        results.append(-1)
        continue
        
    is_ordered = [A_sorted[i] == A[i] for i in range(len(A))]
    first_false = is_ordered.index(False)
    last_false = len(is_ordered) - 1 - is_ordered[::-1].index(False)
    
    # if all the incorrectly ordered elements create a subarray with a N to the left of it and 
    # an S to the right of it or vice versa, then we can reorder all the unordered elements in one move
    if ('N' in polarity[:first_false + 1] and 'S' in polarity[last_false:]) \
        or ('S' in polarity[:first_false + 1] and 'N' in polarity[last_false:]):
            results.append(1)
            
    # otherwise it will take at most two moves to reorder all the elements
    else:
        results.append(2)
        

for result in results:
    print(result)

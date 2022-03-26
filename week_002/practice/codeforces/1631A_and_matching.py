def and_matching(n, k):
    """
    Consider n=8. If we pair [(0, 7), (1, 6), (2, 5), (3, 4)], 
    then the sum of the AND of each pair is 0. Let's call this
    the zero-pair. We will use this as a starting point, knowing 
    that this type of (symmetric) pairing gives us a sum of 0. 

    Then we notice two things:
        1. the greatest number, n - 1, is all one's and &ing it 
        with any other number will give that other number back.
        2. &ing any number with 0 will give 0 back, meaning we 
        can use this to maintain the sum of 0.
    So if we want a sum of k, let's find the zero-pair that contains k
    and then do (n - 1) & k which will give us the number k and 
    0 & (n - 1 - k) which will zero out the pair of k.

    My code is structured so that we are constructing the zero-pairs
    but when we get to the pair that contains the number k 
    (or the number n - 1 - k which is the counterpart of k in k's zero-pair),
    then we will pair k with 1 and the counterpart, n - 1 - k, with 0.
    """

    # initial values
    pairs = []
    k_counter_part = n - 1 - k

    # edge case one
    if k == n - 1:
        pairs.append((-1,))
        return pairs
    
    # edge case two
    if k == 0:
        pairs.append((0, n - 1))

    for i in range(1, n // 2):
        if i == k or i == k_counter_part:
            pairs.append((k, n - 1))
            pairs.append((k_counter_part, 0))
        else:
            pairs.append((i, (n - 1) - i))

    return pairs

def test(pairs):
    return sum([pair[0] & pair[1] for pair in pairs])

n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

    # get inputs
    n, k = [int(x) for x in input().split(' ')]

    # get n/2 pairs of numbers such that summing the AND of each pair equals k
    pairs = and_matching(n, k)
    results.append(pairs)

# print results
for pairs in results:    
    [print(*pair) for pair in pairs]

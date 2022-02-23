# cook your dish here
n_test_cases = int(input())
results = []

for _ in range(n_test_cases):
    
    card_1, card_2 = tuple([int(x) for x in input().split()])
    card_3 = 21 - card_1 - card_2
    results.append(card_3 if card_3 > 0 and card_3 <= 10 else -1)
    
for result in results:
    print(result)

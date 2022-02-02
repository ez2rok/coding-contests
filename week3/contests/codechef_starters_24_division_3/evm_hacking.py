n_test_cases = int(input())
results = []

for _ in range(n_test_cases):

  # get inputs
  x = [int(x) for x in input().split()]
  party_votes = x[:3]
  total_votes = x[3:]

  # find which city can cause the biggest increase the in the number of votes for the party 
  max_diff = 0
  max_city = None
  for city, (n_party_votes, n_total_votes) in enumerate(zip(party_votes, total_votes)):
    diff = n_total_votes - n_party_votes
    if diff > max_diff:
      max_diff = diff
      max_city = city

  # 'hack' the city that can cause the largest increase in the number of votes for the party
  party_votes[max_city] = total_votes[max_city]

  # determine if this will result in a majority
  msg = 'Yes' if sum(party_votes) > sum(total_votes) / 2 else 'No'
  results.append(msg)

for result in results:
  print(result)

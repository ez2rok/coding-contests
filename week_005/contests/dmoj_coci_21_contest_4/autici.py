n_friends = int(input())
road_lengths = [int(x) for x in input().split()]

if len(road_lengths) == 1:
  print(0)

else:
  shortest_road = min(road_lengths)
  sum_ = (sum(road_lengths) - shortest_road) + (len(road_lengths) - 1) * shortest_road
  print(sum_)

from itertools import groupby

class Solution:
    def countCollisions(self, directions: str) -> int:
        
        # get rid of repetitions in directions by storing the direction and how
        # many times that direction appears consequtively, ie store its frequency
        grouped_directions = groupby(directions)
        directions = []
        freqs = []
        for key, group in grouped_directions:
            directions.append(key)
            freqs.append(len(list(group)))  
        
        # initial values
        i = 0
        count = 0
        
        for i in range(len(directions) - 1):
            two_cars = directions[i:i + 2]

            if two_cars == ['R', 'L']:
                count += 2 + max(0, freqs[i] - 1) + max(0, freqs[i+1] - 1)
                directions[i + 1] = 'S' 
            elif two_cars == ['R', 'S']:
                count += freqs[i]
                directions[i + 1] = 'S'
            elif two_cars == ['S', 'L']:
                count += freqs[i + 1]
                directions[i + 1] = 'S'
                
        return count
        

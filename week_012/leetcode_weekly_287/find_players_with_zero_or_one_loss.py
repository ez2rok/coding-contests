from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        winners = []
        losers = []
        
        for match in matches:
            winner, loser = tuple(match)
            winners.append(winner)
            losers.append(loser)
            
        # get players who have never lost
        never_lost = set(winners) - set(losers)
        
        # get players who have only lost once
        player_to_n_losses = Counter(losers)
        lost_once = [player for player, n_losses in player_to_n_losses.items() if n_losses == 1]
        
        return [sorted(never_lost), sorted(lost_once)]
      

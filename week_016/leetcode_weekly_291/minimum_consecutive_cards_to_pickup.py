from collections import defaultdict

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        card_to_idxs = defaultdict(list)
        for i, c in enumerate(cards):
            card_to_idxs[c].append(i)
        
        min_consequtuive_cards = float('inf')
        min_card = -1
            
        for card, idxs in card_to_idxs.items():
            if len(idxs) <= 1:
                continue
            min_consequtuive_cards_ = min([idxs[i] - idxs[i-1] + 1 for i in range(1, len(idxs))])
            
            # update value
            if min_consequtuive_cards_ < min_consequtuive_cards:
                min_consequtuive_cards = min_consequtuive_cards_
                min_card = card
              
        return -1 if min_card == -1 else min_consequtuive_cards

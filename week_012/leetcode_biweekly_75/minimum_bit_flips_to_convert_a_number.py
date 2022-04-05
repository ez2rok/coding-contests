class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        start, goal = bin(start)[2:], bin(goal)[2:]
        if len(start) > len(goal):
            goal = '0' * (len(start) - len(goal)) + goal
        else:
            start = '0' * (len(goal) - len(start)) + start

        return sum([s != g for s, g in zip(start, goal)])

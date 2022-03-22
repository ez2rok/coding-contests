class Solution:   
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        
        # count how many times the characters in the pattern occur
        char_1_occurrences = []
        char_2_occurrences = []

        for i, char in enumerate(text): # O(n)
            if char == pattern[0]:
                char_1_occurrences.append(i)
            if char == pattern[1]:
                char_2_occurrences.append(i)
                        
        
        # count how many subsequences are formed
        n_subsequences = 0
        char_1_idx = char_2_idx = 0
        
        while char_1_idx < len(char_1_occurrences) and char_2_idx < len(char_2_occurrences):
            if char_1_occurrences[char_1_idx] < char_2_occurrences[char_2_idx]:
                n_subsequences += len(char_2_occurrences) - char_2_idx
                char_1_idx += 1
            else:
                char_2_idx += 1
        
        return n_subsequences + max(len(char_1_occurrences), len(char_2_occurrences))

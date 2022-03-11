class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        # initial values
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = []
        
        # get input
        col_1, row_1, _, col_2, row_2 = tuple(list(s))
        
        
        for char in alphabet[alphabet.index(col_1): alphabet.index(col_2) + 1]:
            for num in range(int(row_1), int(row_2) + 1):
                result.append('{}{}'.format(char, num))
                
        return result
        

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        # convert 'HH:MM' to number of minutes (int)
        current_time_in_minutes = int(current[:2]) * 60 + int(current[-2:])
        correct_time_in_minutes = int(correct[:2]) * 60 + int(correct[-2:])
        
        # initial values
        operations = [60, 15, 5, 1]
        n_operations_total = 0
        
        for operation in operations:
            n_operations = (correct_time_in_minutes - current_time_in_minutes) // operation
            
            # update values
            current_time_in_minutes += operation * n_operations
            n_operations_total += n_operations
            
        return n_operations_total

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif numRows == 2:
            indexes = []
            indexes += [s[index] for index in range(0, len(s), 2)]
            indexes += [s[index] for index in range(1, len(s), 2)]
            return ''.join(indexes)
            
        indexes = []
        
        repeat = numRows + (numRows - 2)
        indexes_first = [index for index in range(0, len(s), repeat)]
        indexes_last = [index for index in range(numRows - 1, len(s), repeat)]
        
        indexes_middle = []
        for start_index in range(1, numRows - 1):
            for index in range(start_index, len(s), repeat):
                indexes_middle += [index]
                if index + (repeat - (2 * start_index)) < len(s):
                    indexes_middle += [index + (repeat - (2 * start_index))]
                    
        return (''.join([s[index] for index in indexes_first] + [s[index] for index in indexes_middle] + [s[index] for index in indexes_last]))
        
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diag = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i+j not in diag:
                    diag[i+j] = [matrix[i][j]]
                else:
                    diag[i+j].append(matrix[i][j])
                    
        snake = []
        for entry in diag.items():
            if entry[0] % 2 == 0:
                [snake.append(x) for x in entry[1][::-1]]
            else:
                [snake.append(x) for x in entry[1]]
                
        return snake

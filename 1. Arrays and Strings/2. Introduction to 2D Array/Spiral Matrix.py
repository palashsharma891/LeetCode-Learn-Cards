class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        if len(matrix) == 1: return matrix[0]
        M, N = len(matrix), len(matrix[0])
        n = m = 0
        out = []
        iteration, max_iteration = 0, min(N, M)
        while iteration < max_iteration:
            if iteration % 2 == 0:
                for j in range(n, N):
                    out += [matrix[m][j]]
                for i in range(m+1, M):
                    out += [matrix[i][N-1]]
                m, N = m+1, N-1
            else:
                for j in reversed(range(n, N)):
                    out += [matrix[M-1][j]]
                for i in reversed(range(m, M-1)):
                    out += [matrix[i][n]]
                n, M = n+1, M-1
            iteration += 1
            
        return out

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool: 
        visited = set()
        m, n = len(board), len(board[0])
        def valid(row: int, col: int) -> bool:
            nonlocal m, n, visited
            if row < 0 or row > (m - 1):
                return False
            if col < 0 or col > (n - 1):
                return False
            if (row,  col) in visited:
                return False
            return True

        def explore(current: List[str], row: int, col: int) -> bool:
            nonlocal visited
            if word[len(current)] != board[row][col]:
                return False
            current += board[row][col]
            if len(current) == len(word):
                return True
            visited.add((row, col))

            for r, c in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]:
                if valid(r, c):
                    if explore(current, r, c):
                        return True
            visited.remove((row, col))
            current = current[:len(current) - 1]
            return False
        
        for row in range(0, m):
            for col in range(0, n):
                if explore("", row, col):
                    return True
        return False      
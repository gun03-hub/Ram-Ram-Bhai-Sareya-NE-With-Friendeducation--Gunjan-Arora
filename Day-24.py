#P1-Nearest Exit From a Given Entrance in a Maze 
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([(entrance, 0)])
        maze[entrance[0]][entrance[1]] = '+'
        
        while queue:
            (x, y), step = queue.popleft()
            if [x, y] != entrance and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1):
                return step
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.':
                    queue.append(((nx, ny), step + 1))
                    maze[nx][ny] = '+'
        
        return -1
#P2- Rotting Oranges
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_count -= 1
            minutes += 1
        
        return minutes if fresh_count == 0 else -1

#P1- Keys and Rooms
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False] * len(rooms)
        self.dfs(rooms, 0, visited)
        return all(visited)

    def dfs(self, rooms, room, visited):
        if visited[room]:
            return
        visited[room] = True
        for key in rooms[room]:
            self.dfs(rooms, key, visited)
#P2- Number of Provinces
class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        visited = [False] * n
        count = 0

        def dfs(i):
            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count

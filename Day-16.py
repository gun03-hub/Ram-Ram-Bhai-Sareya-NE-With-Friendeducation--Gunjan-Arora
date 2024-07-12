#P1- Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        self.result = None

        def inorder(node):
            if node:
                inorder(node.left)
                self.count += 1
                if self.count == k:
                    self.result = node.val
                    return
                inorder(node.right)

        inorder(root)
        return self.result
      
#-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X

#P2-Course Schedule II
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses
        order = []

        for y, x in prerequisites:  # Notice the change here
            graph[x].append(y)  # x is a prerequisite for y

        def dfs(i):
            if visited[i] == -1:
                return False  # Cycle detected
            if visited[i] == 1:
                return True  # Already visited
            visited[i] = -1  # Mark as visiting
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1  # Mark as visited
            order.append(i)
            return True

        for i in range(numCourses):
            if visited[i] == 0:  # Only visit unvisited nodes
                if not dfs(i):
                    return []  # If a cycle is detected, return an empty list

        return order[::-1]  # Reverse the order to get the correct topological sort

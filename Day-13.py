# P1-LRU-CACHE
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.order = list()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache) == self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
            self.cache[key] = value
            self.order.append(key)

#P2 - Path Sum
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        def dfs(node, current_sum):
            if not node:
                return False
            current_sum += node.val
            if not node.left and not node.right:
                return current_sum == targetSum
            return dfs(node.left, current_sum) or dfs(node.right, current_sum)
        
        return dfs(root, 0)

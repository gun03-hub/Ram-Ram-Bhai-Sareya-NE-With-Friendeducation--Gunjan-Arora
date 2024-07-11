#P-1 BINARY-TREE-MAXIMUM-PATH-SUM
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = float('-inf')
        def maxPathSumHelper(node):
            if node is None:
                return 0
            left = max(maxPathSumHelper(node.left), 0)
            right = max(maxPathSumHelper(node.right), 0)
            self.maxSum = max(self.maxSum, node.val + left + right)
            return node.val + max(left, right)

        maxPathSumHelper(root)
        return self.maxSum
#P-2 BINARY-TREE-RIGHT-SIDE-VIEW
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

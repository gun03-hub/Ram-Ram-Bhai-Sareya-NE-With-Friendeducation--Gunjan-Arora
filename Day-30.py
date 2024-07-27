#P1- Total cost to hire k workers
import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """
        # Split the costs into two lists: one for the first 'candidates' elements and one for the rest
        costs1 = costs[:candidates]
        costs2 = costs[candidates:]
        
        # Create two heaps to store the costs of the two types of candidates
        heap1 = []
        heap2 = []
        
        # Add the costs to the heaps
        for cost in costs1:
            heapq.heappush(heap1, cost)
        for cost in costs2:
            heapq.heappush(heap2, cost)
        
        # Calculate the total cost by popping elements from the heaps
        total_cost = 0
        for _ in range(k):
            # Pop the smallest cost from the heap with the smaller top element
            if heap1 and heap2:
                if heap1[0] <= heap2[0]:
                    total_cost += heapq.heappop(heap1)
                else:
                    total_cost += heapq.heappop(heap2)
            # If one heap is empty, pop from the other heap
            elif heap1:
                total_cost += heapq.heappop(heap1)
            elif heap2:
                total_cost += heapq.heappop(heap2)
        
        return total_cost
#P2- Count ood Nodes in Binary Tree
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            return count + dfs(node.left, max_val) + dfs(node.right, max_val)

        return dfs(root, float('-inf'))

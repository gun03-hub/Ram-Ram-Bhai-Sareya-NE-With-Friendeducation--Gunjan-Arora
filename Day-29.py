#P1--th Tribonacci Number
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        a, b, c = 0, 1, 1
        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c
        
        return c
#P2- Successful Pairs of Spells and Potions
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        res = []
        potions.sort()
        for spell in spells:
            idx = self.binary_search(potions, (success + spell - 1) // spell if spell != 0 else float('inf'))
            res.append(len(potions) - idx)
        return res

    def binary_search(self, potions, target):
        left, right = 0, len(potions)
        while left < right:
            mid = (left + right) // 2
            if potions[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

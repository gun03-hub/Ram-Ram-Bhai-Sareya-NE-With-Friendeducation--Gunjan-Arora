#P1- 
class Solution(object):
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        # First pass: mark rows and cols that have zeros
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        # Second pass: set zeros in marked rows and cols
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# Test case 1:
matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
Solution().setZeroes(matrix1)
print(matrix1) 

# Test case 2:
matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix2)
print(matrix2) 

#P2-Isomorphic Strings
class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        s_to_t, t_to_s = {}, {}
        
        for i in range(len(s)):
            if s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            elif s_to_t.get(s[i]) != t[i] or t_to_s.get(t[i]) != s[i]:
                return False
        
        return True

# Test case 1:
print(Solution().isIsomorphic("egg", "add")) dfr5

# Test case 2:
print(Solution().isIsomorphic("foo", "bar"))  

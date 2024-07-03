#P1 3Sum
class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result
#Test Case
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

#P2- Rotate Image
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # Reverse each row
        for i in range(n):
            matrix[i] = matrix[i][::-1]

#Test Case      
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
expected_output = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
solution = Solution()
solution.rotate(matrix)
print(f"Input: matrix = {matrix}, Expected Output: {expected_output}, Actual Output: {matrix}")

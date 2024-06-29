#P1- Jump Game 1
class Solution(object):
    def canJump(self, nums):
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(farthest, i + nums[i])
        
        return farthest >= len(nums) - 1

# Test Case
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
solution = Solution()
print("Can jump (example 1):", solution.canJump(nums1))  
print("Can jump (example 2):", solution.canJump(nums2)) 

#--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--

#P2- Jump Game 2
class Solution(object):
    def jump(self, nums):
        n = len(nums)
        max_pos, max_steps, jumps = 0, 0, 0
        for i in range(n - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == max_steps:
                jumps += 1
                max_steps = max_pos
        return jumps

# test case
print(jump([2,3,1,1,4])) 
print(jump([1,1,0,1,1])) 

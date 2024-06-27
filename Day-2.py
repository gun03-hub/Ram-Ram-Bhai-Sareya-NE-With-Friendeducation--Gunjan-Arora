class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# Test the function
nums = [3, 2, 3]
print("The input array for majority element is:", nums)
solution = Solution()
result = solution.majorityElement(nums)
print("Majority element:", result)

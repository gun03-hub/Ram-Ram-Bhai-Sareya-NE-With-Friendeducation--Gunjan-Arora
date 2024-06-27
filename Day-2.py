#P1- Remove Duplicates from Sorted Array
def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1

# Test the function
nums = [1, 1, 2]
print("The original array is:", nums)
length = removeDuplicates(nums)
print("Length without duplicates:", length)
print("Array without duplicates:", nums[:length])

#P2- Majority Elements
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

#P1 FIND-THE-INDEX-OF-THE-FIRST-OCCURRENCE-IN-A-STRING
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1
#Test Case 1:
haystack = "hello"
needle = "ll"
expected_output = 2
assert Solution().strStr(haystack, needle) == expected_output

# Test case 2:
haystack = "aaaaa"
needle = "bba"
expected_output = -1
assert Solution().strStr(haystack, needle) == expected_output


#P2 TWO-SUM-II-INPUT-ARRAY-IS-SORTED

class Solution(object):
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1] 
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []

# Test case 1:
numbers = [2, 7, 11, 15]
target = 9
expected_output = [1, 2]
assert Solution().twoSum(numbers, target) == expected_output

# Test case 2:
numbers = [2, 3, 4]
target = 7
expected_output = [1, 3]
assert Solution().twoSum(numbers, target) == expected_output

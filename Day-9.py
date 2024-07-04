#P1- Group Anagrams
class Solution(object):
    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in res:
                res[sorted_s].append(s)
            else:
                res[sorted_s] = [s]
        return list(res.values())

# -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-

#P2- Happy Number
class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

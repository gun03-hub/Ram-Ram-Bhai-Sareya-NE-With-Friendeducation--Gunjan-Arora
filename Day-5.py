#P1 Gas Station
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        total_gas = 0
        curr_gas = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            curr_gas += gas[i] - cost[i]
            
            if curr_gas < 0:
                start = i + 1
                curr_gas = 0
        
        return start if total_gas >= 0 else -1

 # Test case
print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2])) 
print(canCompleteCircuit([2, 3, 4], [3, 4, 3])) 

#P2- Candy
class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)

#Test case
print(Solution().candy([1, 0, 2]))  
print(Solution().candy([1, 2, 2]))  

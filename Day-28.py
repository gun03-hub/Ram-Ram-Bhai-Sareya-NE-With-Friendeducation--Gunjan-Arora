#P1- Word Ladder
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # Create a set of words for O(1) lookup
        word_set = set(wordList)
        
        # Check if endWord is in the word set
        if endWord not in word_set:
            return 0
        
        # Create a queue for BFS
        queue = deque([(beginWord, 1)])
        
        # Perform BFS
        while queue:
            word, length = queue.popleft()
            
            # If we've reached the endWord, return the length
            if word == endWord:
                return length
            
            # Generate all possible next words
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    
                    # If the next word is in the word set, add it to the queue
                    if next_word in word_set:
                        queue.append((next_word, length + 1))
                        word_set.remove(next_word)
        
        # If we've reached this point, there's no possible ladder
        return 0
#P2- Single number II
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        for num, count in count_map.items():
            if count == 1:
                return num

# P1- Word Ladder
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
      
# -X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X

# P2- Word Search
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit again 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or \
              self.dfs(board, i-1, j, word[1:]) or \
              self.dfs(board, i, j+1, word[1:]) or \
              self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res

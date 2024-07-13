#P1- Snakes and Ladders
from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        visited = {1}
        queue = deque([(1, 0)])  # (position, step)
        while queue:
            pos, step = queue.popleft()
            for jump in range(1, 7):
                next_pos = pos + jump
                if next_pos > n * n:
                    break
                r, c = self.get_position(next_pos, n)
                if board[r][c]!= -1:
                    next_pos = board[r][c]
                if next_pos == n * n:
                    return step + 1
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, step + 1))
        return -1

    def get_position(self, pos, n):
        r = (pos - 1) // n
        c = (pos - 1) % n
        if r % 2 == 1:
            c = n - 1 - c
        return n - 1 - r, c
#P2- Implement Trie (Prefix Tree)
class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

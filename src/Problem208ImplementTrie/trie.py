from collections import defaultdict
from typing import Optional


class TrieNode:
    def __init__(self, letter=None):
        self.children = {}  # {"c" : TrieNode()}
        self.isEnd = False


class Trie:

    def __init__(self):
        # strores { "a" : {"next_letter": ["p"] , is_end: False} }
        self.root = TrieNode()
        return

    def insert(self, word: str) -> None:
        cur: TrieNode = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # get from dictionary
            cur = cur.children[c]  # retrieve the TrieNode()
        cur.isEnd = True  # the last one will get isEnd

        # print(self.root)
        return

    def search(self, word: str) -> bool:
        cur = self.root
        # print(searchNode)

        for c in word:
            if c not in cur.children:
                return False
            # just normally traverse the tree until the end of the `word`
            cur = cur.children[c]

        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        # same logic but less strict than search
        cur = self.root
        # print(searchNode)

        for c in prefix:
            if c not in cur.children:
                return False
            # just normally traverse the tree until the end of the `word`
            cur = cur.children[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # true
print(trie.search("app"))  # false
print(trie.search("kon"))  # false
print(trie.startsWith("app"))  # true
trie.insert("app")
print(trie.search("app"))  # true

print("------------")

trie = Trie()
trie.insert("a")
print(trie.search("a"))  # true
print(trie.startsWith("a"))  # true

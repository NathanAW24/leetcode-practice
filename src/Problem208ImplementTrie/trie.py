from collections import defaultdict
from typing import Optional


class TrieNode:
    def __init__(self, letter=None):
        self.letter = letter
        self.next_letters: set[Optional[TrieNode]] = set()
        self.is_end = False

    def __str__(self):
        return self._str_helper(0)

    def _str_helper(self, level):
        result = "  " * level + \
            f"letter: {self.letter}, is_end: {self.is_end}\n"
        for child in self.next_letters:
            result += child._str_helper(level + 1)
        return result


class Trie:

    def __init__(self):
        # strores { "a" : {"next_letter": ["p"] , is_end: False} }
        self.root = TrieNode()
        return

    def insert(self, word: str) -> None:
        prevLetterNode: TrieNode = self.root
        for idx, letter in enumerate(word):
            letterNode: TrieNode = TrieNode(letter)

            prevLetterNode.next_letters.add(letterNode)
            if idx == 0:
                prevLetterNode = letterNode
            if idx == len(word) - 1:
                print("check is_end", idx)
                letterNode.is_end = True
            else:  # in the middle
                prevLetterNode = letterNode

        # print(self.root)
        return

    def search(self, word: str) -> bool:
        searchNode = self.root
        # print(searchNode)

        for idx, queryLetter in enumerate(word):
            for idx_nextNode, nextNode in enumerate(searchNode.next_letters):
                if queryLetter == nextNode.letter:
                    searchNode = nextNode

                    if idx == len(word)-1:
                        print("check")
                        return searchNode.is_end
                # tydack sama dan sudah terakhir
                elif idx_nextNode == len(searchNode.next_letters)-1:
                    return False  # no nextNode matches query Letter

        return

    def startsWith(self, prefix: str) -> bool:
        searchNode = self.root
        # print(searchNode)

        for idx, queryLetter in enumerate(prefix):
            for idx_nextNode, nextNode in enumerate(searchNode.next_letters):
                if queryLetter == nextNode.letter:
                    searchNode = nextNode

                    if idx == len(prefix)-1:  # prefix is included inside the Trie structure
                        return True
                # tydack sama dan sudah terakhir
                elif idx_nextNode == len(searchNode.next_letters)-1:
                    return False  # no nextNode matches query Letter

        return

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

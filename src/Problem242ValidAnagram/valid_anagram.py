class Solution:

    def __init__(self):
        self.letterDictS = dict()
        self.letterDictT = dict()

    def iterateUpdateDict(self, dictionary, word):
        for letter in word:
            if letter not in dictionary:
                dictionary[letter] = 1
            else:
                dictionary[letter] += 1

    def isAnagram(self, s: str, t: str) -> bool:
        self.iterateUpdateDict(self.letterDictS, s)
        self.iterateUpdateDict(self.letterDictT, t)

        if self.letterDictS == self.letterDictT:
            return True

        return False


s = "anagram"
t = "nagaram"
solution = Solution()
print(solution.isAnagram(s, t))

s = "rat"
t = "car"
solution = Solution()
print(solution.isAnagram(s, t))

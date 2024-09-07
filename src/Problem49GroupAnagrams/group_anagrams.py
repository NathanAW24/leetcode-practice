from typing import List


class Solution:

    def isAnagram(self, str1, str2):  # HELPER
        # str1 and str2 are anagrams if each letter in each string has the same number of appearances

        # modularize this IF GOT TIME
        hash1 = {}
        for letter in str1:
            if letter in hash1:
                hash1[letter] = hash1[letter] + 1
            else:
                hash1[letter] = 1

        hash2 = {}
        for letter in str2:
            if letter in hash2:
                hash2[letter] = hash2[letter] + 1
            else:
                hash2[letter] = 1

        return True if hash1 == hash2 else False

    def hasAnagramInHash(self, hash, string):  # HELPER
        for str_key in hash.keys():
            if self.isAnagram(string, str_key):
                return True, str_key
        return False, string

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            has_anagram, str_key = self.hasAnagramInHash(hash, word)
            if has_anagram:
                hash[str_key].append(word)
            else:
                hash[str_key] = [str_key]

        return list(hash.values())


print(Solution().isAnagram("abcc", "bcca"))  # true
print(Solution().isAnagram("tan", "eat"))
print(Solution().hasAnagramInHash({
    "cba": ["cab"]
}, "abc"))
print(Solution().hasAnagramInHash({}, "abc"))

# test case 1
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
print(solution.groupAnagrams(strs))

# test case 2
strs = [""]
solution = Solution()
print(solution.groupAnagrams(strs))

# test case 3
strs = ["a"]
solution = Solution()
print(solution.groupAnagrams(strs))

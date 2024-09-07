from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}  # key is sorted word string, value is array of anagrams

        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word in hash:
                hash[sorted_word].append(word)
            else:
                hash[sorted_word] = [word]

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

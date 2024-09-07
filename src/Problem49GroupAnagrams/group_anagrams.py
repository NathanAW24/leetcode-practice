from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key is sorted word string, value is array of anagrams
        hash = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord('a')] += 1

            hash[tuple(count)].append(word)

        return hash.values()


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

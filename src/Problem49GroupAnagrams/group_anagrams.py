from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}  # key is sorted word string, value is array of anagrams

        for word in strs:
            count = [0 for i in range(26)]

            for letter in word:
                ascii_letter = ord(letter)
                ascii_a = ord('a')
                idx = ascii_letter - ascii_a

                count[idx] = count[idx] + 1

            if tuple(count) in hash:
                hash[tuple(count)].append(word)
            else:
                hash[tuple(count)] = [word]

        return list(hash.values())


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

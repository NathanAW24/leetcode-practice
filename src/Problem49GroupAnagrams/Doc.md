# Problems Faced
## Problem 1: `AttributeError: 'NoneType' object has no attribute 'append'`
```python

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
        for letter in str1:
            if letter in hash2:
                hash2[letter] = hash2[letter] + 1
            else:
                hash2[letter] = 1

        return True if hash1 == hash2 else False

    def hasAnagramInHash(self, hash, string):
        for str_key in hash.keys():
            if self.isAnagram(string, str_key):
                return True, str_key
        return False, string

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            has_anagram, str_key = self.hasAnagramInHash(hash, word)
            print(f"hash: {hash}")
            if has_anagram:
                "has anagram"
                hash[str_key] = hash[str_key].append(word)
            else:
                "! has anagram"
                hash[str_key] = [str_key]

        return list(hash.values())

...

# test case 1
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
assert solution.groupAnagrams(
    strs) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

```

Why that error appears given log?
```bash
hash: {}
hash: {'eat': ['eat']}
hash: {'eat': None}
```

Why is the value `None` there?

Mistake is in this line
```python
...
hash[str_key] = hash[str_key].append(word)
...
```
This replaces the whole `hash[str_key]` into `hash[str_key].append(word)`, and just fyi, it the function `.append(...)` appends the list but returne `None`.


## Problem 2: `hasAnagramInHash` returns `True` for `'tan'` when key is `'eat'`
```python
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
        for letter in str1:
            if letter in hash2:
                hash2[letter] = hash2[letter] + 1
            else:
                hash2[letter] = 1

        return True if hash1 == hash2 else False

    def hasAnagramInHash(self, hash, string):
        for str_key in hash.keys():
            if self.isAnagram(string, str_key):
                return True, str_key
        return False, string

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for word in strs:
            has_anagram, str_key = self.hasAnagramInHash(hash, word)
            print(f"hash: {hash}")
            if has_anagram:
                print("has anagram")
                hash[str_key].append(word)
            else:
                print("! has anagram")
                hash[str_key] = [str_key]

        return list(hash.values())

...

# test case 1
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
assert solution.groupAnagrams(
    strs) == [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

```

Logging this returns `True`
```python
print(Solution().isAnagram("tan", "eat")) # True but should be False instead
```

Function `isAnagram` is wrong!
I am iterating over `str1` for `hash2`, should be `str2` in this line
```python
...        
    hash2 = {}
    for letter in str1:
...
```
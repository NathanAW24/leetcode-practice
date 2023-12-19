from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # {sumValue: {how many times sumValue appears}}
        # {0: 1} case, is edge case for when sumFrom(nums[0]...nums[i]) == k directly
        # it represents the empty subarray behind the first element
        noOfSumValueHash = {0: 1}
        count = 0
        thisIterationSum = 0

        for i in range(len(nums)):
            # sum of array from nums[0]...nums[i] inclusive
            thisIterationSum = thisIterationSum + nums[i]

            # COUNT ADDITION STEP
            # want to find ==> subarraySum == k
            # sumFrom(nums[j+1]...nums[i]) = k, abaikan spesifik index-nya
            # sumFrom(nums[0]...nums[i]) - sumFrom(nums[0]..nums[j]) = k
            # sumFrom(thisIteration) - sumFrom(previousIteration) = k
            # sumFrom(previousIteration) = sumFrom(thisIteration) - k
            prevIterationSum = thisIterationSum - k
            # check if sumFrom(previousIteration) is recorded alr
            # the sum value from previousIteration subarrays can appear more than 1 time
            if prevIterationSum in noOfSumValueHash:
                count = count + noOfSumValueHash[prevIterationSum]

            # PUT IN DICTIONARY STEP
            # here thisIterationSum is sumFrom(nums[0]...nums[i]) = sumFrom(thisIteration)
            # then this will be recorded
            # next iteration(s) this recorded value appear as sumFrom(previousIteration) = sumForm(nums[0]...nums[i])
            #
            # e.g.
            # iteration i = 2, k = 6
            # found thisIterationSum = 4
            # ... stuff with prevIterationSum (neglect this for now), assuming prevIterationSum not in dict
            # put/update thisIterationSum in dict { ..., 4: *someInt ,...}
            # iteration i = 3
            # found thisIterationSum = 10
            # prevIterationSum = 4, which is the value of the previous thisIterationSum
            # goes to the {count += *someInt} block
            if thisIterationSum not in noOfSumValueHash:
                noOfSumValueHash[thisIterationSum] = 1
            else:  # thisIterationSum has appeared previously as prevIterationSum, hence increment only...
                # basically saying to the next iteration(s) there is more than one iterationSum arrays, that results in same value
                # the next iteration(s) that satisfies conditions, can work with all of those iterationSum arrays
                noOfSumValueHash[thisIterationSum] = noOfSumValueHash[thisIterationSum] + 1
                # more accurate formula below, but values are same (prevIterationSum == thisIterationSum) so ...
                # noOfSumValueHash[prevIterationSum] = noOfSumValueHash[thisIterationSum] + 1
        return count


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 3, 4, 2, 2, 1]
    k = 4
    print("Test Case 1")
    print(solution.subarraySum(nums, k))
    nums = [1, 1, 1]
    k = 2
    print("Test Case 2")
    print(solution.subarraySum(nums, k))
    nums = [1, 2, 3]
    k = 3
    print("Test Case 3")
    print(solution.subarraySum(nums, k))

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nathan
        max_idxs = {
            "first": None,
            "second": None,
            "third": None
        }

        for i in range(len(nums)):
            if nums[i] == max_idxs["first"] or nums[i] == max_idxs["second"] or nums[i] == max_idxs["third"]:
                continue
            elif max_idxs["first"] == None or nums[i] > max_idxs["first"]:
                max_idxs["third"] = max_idxs["second"]
                max_idxs["second"] = max_idxs["first"]
                max_idxs["first"] = nums[i]
            elif max_idxs["second"] == None or nums[i] > max_idxs["second"]:  # < first
                max_idxs["third"] = max_idxs["second"]
                max_idxs["second"] = nums[i]
            elif max_idxs["third"] == None or nums[i] > max_idxs["third"]:  # < second
                max_idxs["third"] = nums[i]

        # print(max_idxs)

        max_val = 0
        if max_idxs["third"] == None:
            max_val = max_idxs["first"]
            # print(max_val)
        else:
            max_val = max_idxs["third"]
            # print(max_val)

        return max_val


if __name__ == "__main__":
    solution = Solution()

    nums1 = [3, 2, 1]
    print(solution.thirdMax(nums1))

    nums2 = [1, 2]
    print(solution.thirdMax(nums2))

    nums3 = [2, 2, 3, 1]
    print(solution.thirdMax(nums3))

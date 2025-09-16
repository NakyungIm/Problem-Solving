# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            j = i + nums[i:].index(min(nums[i:]))
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
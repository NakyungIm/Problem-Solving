# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        result = False
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                result = True
        return result
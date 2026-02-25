# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
            else: pass
        return False
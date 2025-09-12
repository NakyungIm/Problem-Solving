# https://leetcode.com/problems/majority-element/
# Sorting

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
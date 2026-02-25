# https://leetcode.com/problems/majority-element/
# O(n) time complexity, O(1) space complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = 0
        max_value = 0
        for i in nums:
            if max_value == 0: result = i
            if i == result:
                max_value += 1
            else: max_value += -1
        return result
        
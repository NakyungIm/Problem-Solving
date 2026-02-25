# https://leetcode.com/problems/majority-element/
# O(n) time complexity, O(n) space complexity

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        max_value = 0
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
            if count[i] > max_value:
                result = i
                max_value = count[i]
        return result
        
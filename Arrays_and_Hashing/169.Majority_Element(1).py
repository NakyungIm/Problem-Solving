# https://leetcode.com/problems/majority-element/
# Hash Table

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {} # Key: number, Value: count
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
  
        # First solution
        max_value = max(count.values())
        for key, val in count.items():
            if val == max_value:
                result = key
        return result

        # Second solution
        # if max(count.values()) > len(nums)/2:
        #     result = [key for key, val in count.items() if val == max(count.values())]
        #     return result[0]
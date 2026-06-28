class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_= {}

        for i in nums:
            dict_[i] = dict_.get(i, 0) + 1

        return min(dict_, key=dict_.get)

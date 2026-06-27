class Solution:
    def majorityElement(self, nums):
        dict_= {}

        for i in nums:
            dict_[i] = dict_.get(i, 0) + 1

        return max(dict_, key=dict_.get)

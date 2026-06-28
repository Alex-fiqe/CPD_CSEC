class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=0
        r=n
        k=[]
        while r<len(nums):
            k.append(nums[l])
            k.append(nums[r])
            l+=1
            r+=1
        return k

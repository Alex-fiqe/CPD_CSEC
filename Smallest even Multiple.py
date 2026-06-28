class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        b=2
        m=n
        k=b
        while k!=m:
            if m<k:
                 m+=n
            else: 
                k+=b
        return m

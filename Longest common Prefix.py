class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        ans = ""

        for i in range(len(first)):
            if i < len(last) and first[i] == last[i]:
                ans += first[i]
            else:
                break

        return ans

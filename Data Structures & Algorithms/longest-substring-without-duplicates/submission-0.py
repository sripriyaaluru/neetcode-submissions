class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window/two pointer
        charSet=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            res=max(res,r-l+1)

        return res

        #Note: remove l when duplicates (shrink window), and move r when unique (expand window))        
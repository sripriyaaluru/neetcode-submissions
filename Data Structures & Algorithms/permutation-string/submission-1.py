from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count=Counter(s1) #hashmap of s1
        #{a:1,b:1,c:1}
        window=Counter(s2[:len(s1)]) #current window
        l,r=0,len(s1)
        while r<len(s2):
            if window==count:
                return True
            window[s2[l]]-=1
            if window[s2[l]]==0:
                del window[s2[l]]
            window[s2[r]]+=1
            l+=1
            r+=1
        if window==count:
            return True
            
        return False






        

        
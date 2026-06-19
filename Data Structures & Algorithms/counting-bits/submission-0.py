class Solution:
    def countBits(self, n: int) -> List[int]:
        count=[0]*(n+1)
        for i in range(1,n+1):
            j=i
            while j>0:
                if j&1==1:
                    count[i]+=1
                j=j>>1
        return count

        

        
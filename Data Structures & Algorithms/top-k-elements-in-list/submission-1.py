import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #min heap
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        heap=[]
        for num,cnt in count.items():
            heapq.heappush(heap,(cnt,num))
        
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
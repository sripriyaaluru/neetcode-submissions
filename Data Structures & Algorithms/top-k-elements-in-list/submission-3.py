import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        heap=[]
        for num,cnt in hashmap.items():
            heapq.heappush(heap,(cnt,num))

            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



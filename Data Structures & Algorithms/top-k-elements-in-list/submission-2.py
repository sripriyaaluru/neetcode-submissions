class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #array of nums
        #an integer k
        hashmap=defaultdict(int)
        res=[]
        arr=[]
        for i in range(len(nums)):
            hashmap[nums[i]]+=1
        for num,cnt in hashmap.items():
            arr.append([cnt,num])
        arr.sort()
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

            
            


        
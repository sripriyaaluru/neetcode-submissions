import heapq
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        #can be optimized further see that
        heap=[]
        for w in range(len(workers)):
            for b in range(len(bikes)):
                distance=abs(workers[w][0]-bikes[b][0])+abs(workers[w][1]-bikes[b][1])
                heapq.heappush(heap,(distance,w,b))
        
        result=[-1]*len(workers)
        assigned_workers=set()
        used_bikes=set()
        while heap and len(assigned_workers)<len(workers):
            distance,worker,bike=heapq.heappop(heap)
            if worker in assigned_workers or bike in used_bikes:
                continue
            result[worker]=bike
            assigned_workers.add(worker)
            used_bikes.add(bike)
        return result


            

        




        
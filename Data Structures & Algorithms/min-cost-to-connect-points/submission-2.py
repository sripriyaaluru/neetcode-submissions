import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #shortest path
        #MST (Prim's)
        n=len(points)
        minHeap=[(0,0)]
        totalCost=0
        visited=set()
        while len(visited)<n:
            cost,i=heapq.heappop(minHeap)
            if i in visited: 
                continue
            visited.add(i)
            totalCost+=cost
            x1,y1=points[i]
            for j in range(n):
                if j not in visited:
                    x2,y2=points[j]
                    weight=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(minHeap,(weight,j))
        return totalCost







        
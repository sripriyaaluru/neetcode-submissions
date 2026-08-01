from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #MST
        #dijkstra
        #graph=times
        #time=weight
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        minHeap=[(0,k)] #distance,node
        dist=[float("inf")]*(n+1)
        dist[k]=0
        while minHeap:
            currDist,node=heapq.heappop(minHeap)
            if currDist>dist[node]:
                continue
            for neighbour,weight in graph[node]:
                newDist=currDist+weight
                if newDist<dist[neighbour]:
                    dist[neighbour]=newDist
                    heapq.heappush(minHeap,(newDist,neighbour))
        ans=max(dist[1:])
        return -1 if ans==float("inf") else ans





        
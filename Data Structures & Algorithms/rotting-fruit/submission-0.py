from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        time=0
        fresh=0
        #count number of rotten and fresh oranges and add all the rotten oranges to queue(multi-source bfs)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append((r,c))
        
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        while queue and fresh>0:
            length=len(queue)
            #only current oranges can infect at a time
            for i in range(length):
                r,c=queue.popleft()
                for dr,dc in directions:
                    row,col=r+dr,c+dc
                    if (row in range(len(grid)) and col in range(len(grid[0])) and grid[row][col]==1):
                        grid[row][col]=2
                        queue.append((row,col))
                        fresh-=1
            
            time+=1

        return time if fresh==0 else -1


        

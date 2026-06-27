class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #2D Memoization (Top-Down)
        memo=[[-1]*n for i in range(m)]
        def memoization(r,c):
            if r>=m or c>=n:
                return 0
            """out of bounds and no 
            valid path form out of bounds
            to destination so we return 0"""
                 
            if memo[r][c]!=-1:
                return memo[r][c] #saves us
                #from doing repeated work
            if r==m-1 and c==n-1:
                return 1
            
            memo[r][c]=(memoization(r+1,c)+memoization(r,c+1))

            return memo[r][c]
        
        return memoization(0,0)
            
            
            
            
        

        
        
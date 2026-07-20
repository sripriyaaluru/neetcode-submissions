class Solution:
    def rob(self, nums: List[int]) -> int:
        #dynamic programming top down:
        #at each position we have two options: 
        #rob the current house and rob i+2 
        #or skip the current one
        #recursive too slow so we add memoization

        memo=[-1]*len(nums)

        def dfs(i):
            if i>=len(nums):
                return 0
            if memo[i]!=-1:
                return memo[i]
            memo[i]=max(dfs(i+1),nums[i]+dfs(i+2))
            return memo[i]
        return dfs(0)

        

        """

        top down:
        cache=[-1]*len(nums)
        def memoization(i):
            if i>=len(nums):
                return 0
            if cache[i]!=-1:
                return cache[i]
            cache[i]=max(memoization(i+1),nums[i]+memoization(i+2))
            return cache[i]
        return memoization(0)

        bottom up:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],nums[i]+dp[i-2])
        
        return dp[n-1]


        """

        
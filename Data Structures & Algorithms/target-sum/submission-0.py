class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def dfs(i,sums):
            if i==len(nums):
                return 1 if sums==target else 0
            if (i,sums) in memo:
                return memo[(i,sums)]
            memo[(i,sums)]=dfs(i+1,sums+nums[i])+dfs(i+1,sums-nums[i])
            res=memo[(i,sums)]
            return res
        return dfs(0,0)


        
        
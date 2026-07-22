class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2

        def dfs(i,current_sum): #where i is the partition point
            if current_sum==target:
                return True
            if i==len(nums):
                return False
            if (i,current_sum) in memo:
                return memo[(i,current_sum)]
            take=dfs(i+1,current_sum+nums[i])
            skip=dfs(i+1,current_sum)
            memo[(i,current_sum)]=take or skip
            return memo[(i,current_sum)]
        return dfs(0,0)

    
            
            
            
            
            





        
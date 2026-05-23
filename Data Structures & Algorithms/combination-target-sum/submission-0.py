class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(nums) or total>target:
                return
        
            cur.append(nums[i])
            dfs(i,cur,total+nums[i]) #take the number
            cur.pop() #backtracking
            dfs(i+1,cur,total) #skip the number so we do not keep repeating same number

        dfs(0,[],0)
        return res


        
 

       



        


     

       
        




    
    
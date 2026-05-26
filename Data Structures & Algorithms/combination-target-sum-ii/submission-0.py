class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()
        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i>=len(candidates) or total>target:
                return
            
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i]) #no duplicates allowed whereas in combinationSumI they are allowed 
            cur.pop() #backtrack
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1 #decide not to take a value then skip all duplicates of it so we dont get duplicate combinations
            dfs(i+1,cur,total) #skip the value
        dfs(0,[],0) #initial
        return res


        

        


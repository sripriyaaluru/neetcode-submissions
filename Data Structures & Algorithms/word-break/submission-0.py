class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #difficult and a bit confusing dp
        memo={} #Note that memo is not required in shown examples only if theres more than one way to reach the end like s="aaaaa" and wordDict=["a","aa","aaaa"]
        def dfs(i): # can the remainder be segmented
            if i==len(s):
                return True
            if i in memo:
                return memo[i] # if more than one way
            for word in wordDict:
                if (i+len(word))<=len(s) and s[i:i+len(word)]==word:
                    if dfs(i+len(word)):
                        memo[i]=True #memo[8]=True
                        return True #dfs(5) is True
            
            memo[i]=False
            return False

        return dfs(0)
                                


        


        
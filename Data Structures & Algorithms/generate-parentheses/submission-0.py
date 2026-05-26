class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def backtrack(openN, closedN):
            if openN==closedN==n:
                res.append("".join(stack))
                return
            if openN<n:
                stack.append("(") #make a decision
                backtrack(openN+1,closedN) #backtrack
                stack.pop() #undo decision
            if closedN<openN:
                stack.append(")") #make a decision
                backtrack(openN,closedN+1) #backtrack
                stack.pop() #undo decision
        

        backtrack(0, 0)
        return res

        


       


        



















         #sés impossiblé

        """
        algorithm:
        backtracking vs. dynamic programming approach
        backtracking approach is better

        """
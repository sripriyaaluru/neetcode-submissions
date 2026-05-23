class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=[]
        for p,s in zip(position,speed):
            pair.append([p,s])
        pair.sort(reverse=True)
        
        stack=[]
        #in stack we append time to see whether they can merge to form a fleet

        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]: #stack[-1] is top
                stack.pop()
        return len(stack)
                 



        
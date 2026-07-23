
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks) #Counter automatially counts frequencies
        maxFrequency=max(count.values())
        countMax=0
        for freq in count.values():
            if freq==maxFrequency:
                countMax+=1
        return max(len(tasks),(maxFrequency-1)*(n+1)+countMax)

        
        




        



    
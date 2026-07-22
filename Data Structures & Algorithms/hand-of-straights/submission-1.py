class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=defaultdict(int)
        for i in range(len(hand)):
            count[hand[i]]+=1
        hand.sort()
        for num in hand:
            if count[num]==0:
                continue
            
            for j in range(num,num+groupSize):
                if count[j]==0:
                    return False
                count[j]-=1
        return True


        

            



        
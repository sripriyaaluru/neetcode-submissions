class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #hashing
        seen=set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

        

        
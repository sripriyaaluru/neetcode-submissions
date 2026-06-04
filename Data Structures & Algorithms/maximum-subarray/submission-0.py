class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #kadane's algorithm (most popular approach)
        #bottom up apprach
        maxsum=nums[0]
        cursum=0
        for num in nums:
            cursum=max(cursum,0)
            cursum+=num
            maxsum=max(maxsum,cursum)
        return maxsum

        #O(n) time complexity

        #can use sliding window for returning index
        
        

        
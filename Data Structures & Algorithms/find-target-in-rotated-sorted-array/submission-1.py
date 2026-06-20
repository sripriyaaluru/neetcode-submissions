class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
    
        def findMin(nums):
            low=0
            high=len(nums)-1
            while low<high:
                mid=(low+high)//2
                if nums[mid]<nums[high]:
                    high=mid
                else:
                    low=mid+1
            return low

        low=findMin(nums)
        
        l1=low
        r1=len(nums)-1
        l2=0
        r2=low-1
        while l1<=r1:
            m1=(l1+r1)//2
            if target==nums[m1]:
                return m1
            elif target>nums[m1]:
                l1=m1+1
            else:
                r1=m1-1
        
        while l2<=r2:
            m2=(l2+r2)//2
            if target==nums[m2]:
                return m2
            elif target>nums[m2]:
                l2=m2+1
            else:
                r2=m2-1
        
        return -1

        
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(k):
            t = 0
            for x in piles:
                t += (x + k - 1) // k
            return t <= h

        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (l + r) // 2
            if ok(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #no cycle should exist
        # cycle detection
        preMap={i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visiting=set()
        def dfs(crs):
            if crs in visiting:
                return False
                #cycle has been detected
            if preMap[crs]==[]:
                return True
            visiting.add(crs) #checking this crs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs) #done checking this crs
            preMap[crs]=[] #nothing left to check
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True








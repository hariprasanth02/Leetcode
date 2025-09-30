class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def sub_dup(start,path):
           result.append(path[:])
           for i in range(start,len(nums)):
            if i>start and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            sub_dup(i+1,path)
            path.pop()

        sub_dup(0,[])
        return result
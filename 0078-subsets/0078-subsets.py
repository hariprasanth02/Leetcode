class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result =[]
        def sub_set(start,path):
            result.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                sub_set(i+1,path)
                path.pop()
        sub_set(0,[])
        return result
        
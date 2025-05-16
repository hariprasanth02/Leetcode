class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxprod =nums[0]
        minprod=nums[0]
        result=maxprod
        for i in range(1,len(nums)):
            curr = nums[i]
            temp=max(curr,maxprod*curr,minprod*curr)
            minprod=min(curr,maxprod*curr,minprod*curr)
            maxprod=temp
            result=max(result,maxprod)
        return result
        
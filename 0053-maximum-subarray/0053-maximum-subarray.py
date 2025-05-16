class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum =float('-inf')
        currsum=0
        start=0
        end=0
        n=len(nums)
        while end<n:
            while currsum<0:
                currsum -=nums[start]
                start +=1
            currsum += nums[end]
            end+=1
            maxsum=max(maxsum,currsum)
        return maxsum

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            
            l, r = i + 1, n - 1
            
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.append([nums[i], nums[l], nums[r]])

                   
                    while l < r and nums[l] == nums[l + 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r - 1]: 
                        r -= 1
                    
                    l += 1
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1

        return res
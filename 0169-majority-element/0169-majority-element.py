class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majorityElement = -1
        votes = 0
        for i in nums:
            if votes == 0:
                majorityElement = i
                votes = 1
            else:
                if majorityElement == i:
                    votes +=1
                else:
                    votes -=1
        return majorityElement
        
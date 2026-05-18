class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        complements = {}

        for i, n in enumerate(nums):
            if n in complements:
                return [complements[n], i]
            complements[target - n] = i



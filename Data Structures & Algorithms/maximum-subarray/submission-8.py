class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
 
        maxSum = nums[0]
        tempSum = 0

        for r in range(len(nums)):
            if tempSum < 0:
                tempSum = 0
            tempSum += nums[r]
            maxSum = max(maxSum, tempSum)

        return maxSum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,-1,0,1,1,2]

        output = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                zeroSum = nums[i] + nums[l] + nums[r]
                if zeroSum > 0:
                    r -= 1
                elif zeroSum < 0:
                    l += 1
                else:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        
        return output






















'''        nums.sort()
        res = []

        for i, n in enumerate(nums):

            if i > 0 and nums[i - 1] == n:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                
                if n + nums[l] + nums[r] > 0:
                    r -= 1
                elif n + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
            
        return res'''
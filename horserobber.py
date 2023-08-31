#198. House Robber

class Solution:
    def rob(self, nums):
        houses = len(nums)
        if houses == 1:
            return nums[0]
        if houses == 2:
            return max(nums[0], nums[1])

        robbed = nums
        robbed[1] = max(nums[0], nums[1]) #robbed 1st or 2nd house

        for i in range(2, houses):
            robbed[i] = max(robbed[i-1], nums[i] + robbed[i-2])
        return robbed[-1]

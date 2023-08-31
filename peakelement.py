#162. Find Peak Element

class Solution:
    def findPeakElement(self, nums):
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        while left<=right:
            mid=(left+right)>>1
            if (mid==0 or nums[mid]>=nums[mid-1] ) and (mid==len(nums)-1 or nums[mid]>=nums[mid+1]) :
                return mid
            elif nums[mid]<=nums[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1

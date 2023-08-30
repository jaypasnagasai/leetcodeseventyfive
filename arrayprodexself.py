# 238. Product of Array Except Self

class Solution:
  def productExceptSelf(self, nums):
    n = len(nums)
    ans = [1] * n

    # Calculate prefix products and store in ans array
    for i in range(1, n):
      ans[i] = ans[i - 1] * nums[i - 1]

    suffix = 1  # Initialize suffix product
    # Update ans array with suffix products
    for i, num in reversed(list(enumerate(nums))):
      ans[i] *= suffix
      suffix *= num

    return ans

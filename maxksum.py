#1679. Max Number of K-Sum Pairs

class Solution:
  def maxOperations(self, nums, k):
    count = collections.Counter(nums)
    return sum(min(count[num], count[k - num])
               for num in count) // 2

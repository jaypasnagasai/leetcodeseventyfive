#136. Single Number

class Solution:
  def singleNumber(self, nums):
    return functools.reduce(lambda x, y: x ^ y, nums, 0)

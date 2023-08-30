#1493. Longest Subarray of 1's After Deleting One Element

class Solution:
  def longestSubarray(self, nums):
    ans = 0  # Variable to store the length of the longest subarray with at most one zero.
    count0 = 0  # Counter to keep track of the number of zeros in the current subarray.

    l = 0  # Left pointer of the sliding window.
    for r, num in enumerate(nums):  # Iterate through the array using a sliding window approach.
      if num == 0:
        count0 += 1  # Increment the zero count if the current element is zero.
      
      while count0 == 2:  # Shrink the subarray if there are more than one zero.
        if nums[l] == 0:
          count0 -= 1  # Decrement the zero count as a zero is being removed from the subarray.
        l += 1  # Move the left pointer to the right to shrink the subarray.
      
      ans = max(ans, r - l)  # Update the maximum subarray length with at most one zero.

    return ans  # Return the length of the longest subarray with at most one zero.

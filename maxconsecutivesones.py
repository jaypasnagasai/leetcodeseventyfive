#1004. Max Consecutive Ones III

class Solution:
  def longestOnes(self, nums, k):
    ans = 0  # Initialize the variable to store the maximum length of consecutive ones.

    l = 0  # Initialize the left pointer for the sliding window.
    for r, num in enumerate(nums):  # Iterate through the array using a right pointer (r) and the corresponding number (num).
      if num == 0:  # If the current number is 0, decrement k (the number of allowed 0s).
        k -= 1

      while k < 0:  # If the number of allowed 0s (k) becomes negative, meaning we have too many 0s in the window.
        if nums[l] == 0:  # If the number at the left end of the window is 0, increment k (since we're moving the window).
          k += 1
        l += 1  # Move the left pointer to shrink the window and remove the leftmost element.

      ans = max(ans, r - l + 1)  # Calculate the current window's length and update 'ans' if the current length is greater.

    return ans  # Return the maximum length of consecutive ones considering the given number of allowed 0s.

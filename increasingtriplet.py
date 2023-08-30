# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums):
        # Initialize two variables to store the smallest and second smallest values
        first = second = float('inf') 

        # Iterate through each number in the 'nums' array
        for n in nums: 
            # If the current number is smaller than or equal to the 'first' value,
            # update 'first' to the current number.
            if n <= first: 
                first = n
            # If the current number is greater than 'first' but smaller than or equal
            # to the 'second' value, update 'second' to the current number.
            elif n <= second:
                second = n
            # If the current number is greater than both 'first' and 'second', then
            # we have found a valid triplet, and we return True.
            else:
                return True
        
        # If no valid triplet is found after iterating through the entire array,
        # return False.
        return False

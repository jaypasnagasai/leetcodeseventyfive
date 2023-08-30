#283. Move Zeroes

class Solution:
    def moveZeroes(self, nums):
        j = 0  # Initialize a pointer 'j' to keep track of the non-zero elements' position

        # Iterate through the 'nums' array
        for num in nums:
            if num != 0:
                nums[j] = num  # Move the non-zero element to the current 'j' position
                j += 1  # Move the pointer 'j' ahead to the next position

        # After the above loop, all non-zero elements have been moved to the beginning.
        # Now fill the remaining positions with zeros.
        for i in range(j, len(nums)):
            nums[i] = 0  # Fill the remaining positions with zeros

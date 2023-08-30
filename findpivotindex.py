#724. Find Pivot Index

class Solution:
    def pivotIndex(self, nums):
        # Calculate the total sum of the input list 'nums'
        summ = sum(nums)
        # Initialize a variable to keep track of the prefix sum
        prefix = 0
        
        # Iterate through the list using enumeration to access both index and value
        for i, num in enumerate(nums):
            # Check if the current index is a pivot point (prefix sum equals to sum after pivot)
            if prefix == summ - prefix - num:
                return i  # Return the index of the pivot point
            prefix += num  # Update the prefix sum
            
        # If no pivot point is found, return -1
        return -1

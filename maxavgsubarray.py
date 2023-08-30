#643. Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        if len(nums) == 1:
            return float(nums[0])
        
        start = 0
        end = k
        average = 0.0
        
        # Calculate the average of the first window
        for i in range(k):
            average += float(nums[i]) / k
        
        # Initialize the maximum average
        max_average = average
        
        # Slide the window and update the maximum average
        while end < len(nums):
            # Remove the leftmost element from the window and adjust the average
            average = average - float(nums[start]) / k
            # Add the rightmost element to the window and adjust the average
            average = average + float(nums[end]) / k
            # Update the maximum average if the current average is larger
            max_average = max(max_average, average)
            # Move the window by increasing both start and end pointers
            start += 1
            end += 1
        
        return max_average

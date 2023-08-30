#11. Container With Most Water

class Solution:
    def maxArea(self, height):
        # Initialize a variable to store the maximum area
        ans = 0
        
        # Initialize two pointers for the left and right boundaries
        l = 0
        r = len(height) - 1
        
        # Iterate until the left pointer crosses the right pointer
        while l < r:
            # Determine the minimum height of the two boundaries
            minHeight = min(height[l], height[r])
            
            # Calculate the current area using the minimum height and the distance between the boundaries
            currentArea = minHeight * (r - l)
            
            # Update the maximum area if the current area is greater
            ans = max(ans, currentArea)
            
            # Move the pointer that points to the smaller boundary height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        # Return the maximum area
        return ans

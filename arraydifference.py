#2215. Find the Difference of Two Arrays

# Define a class named Solution that contains a method findDifference.
class Solution:
  def findDifference(self, nums1, nums2):
    # Convert the input lists nums1 and nums2 into sets to eliminate duplicates.
    set1 = set(nums1)
    set2 = set(nums2)
    
    # Calculate the set differences between set1 and set2, and vice versa.
    # This finds elements that are present in one set but not in the other.
    result = [set1 - set2, set2 - set1]
    
    # Return the list containing the set differences.
    return result

#1207. Unique Number of Occurrences

class Solution:
    def uniqueOccurrences(self, arr):
        nums = []          # List to store unique numbers encountered
        occurrences = []   # List to store unique occurrences
        
        for num in arr:    # Iterate through the input array
            if num not in nums:  # Check if the number is encountered for the first time
                occurrence = arr.count(num)  # Count how many times the current number appears in the array
                
                if occurrence not in occurrences:  # Check if this occurrence count is unique
                    occurrences += [occurrence]   # If unique, add the occurrence count to the list
                    nums += [num]                 # Also add the number to the list of unique numbers
                else:
                    return False  # If occurrence count is not unique, return False
                
        return True  # If all numbers have unique occurrence counts, return True


#1207. Unique Number of Occurrences

# Import the collections module to use the Counter class
import collections

# Define a class named Solution
class Solution:
  # Define a method named uniqueOccurrences that takes a list 'arr' as input
  def uniqueOccurrences(self, arr):
    # Create a Counter object to count the occurrences of each element in 'arr'
    count = collections.Counter(arr)
    
    # Create an empty set to store unique occurrences
    occurrences = set()

    # Loop through the values (occurrence counts) in the Counter object
    for value in count.values():
      # Check if the value (occurrence count) is already in the 'occurrences' set
      if value in occurrences:
        # If a value is already present, it means a duplicate occurrence count exists
        return False
      
      # If the value is not already in 'occurrences', add it to the set
      occurrences.add(value)

    # If all occurrence counts are unique, return True
    return True

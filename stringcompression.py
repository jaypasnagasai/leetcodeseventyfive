#443. String Compression

class Solution:
  def compress(self, chars):
    ans = 0  # Initialize a pointer for the compressed string
    i = 0    # Initialize a pointer for iterating through the input characters

    while i < len(chars):
      letter = chars[i]  # Store the current character being compressed
      count = 0          # Initialize a counter for consecutive occurrences of the character

      # Count the consecutive occurrences of the current character
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1

      chars[ans] = letter  # Store the compressed character in the output
      ans += 1             # Move the output pointer to the next position

      if count > 1:
        # If the character occurred more than once, convert the count to a string
        # and store each digit of the count as a separate character in the output
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans  # Return the length of the compressed output string

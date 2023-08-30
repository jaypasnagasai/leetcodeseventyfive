#1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s, k):
        ans = 0          # Initialize the maximum count of consecutive vowels.
        maxi = 0          # Initialize the current count of consecutive vowels.
        kVowels = 'aeiou' # String containing the vowels.

        for i, c in enumerate(s):  # Iterate through the characters in the string 's'.
            if c in kVowels:       # If the current character is a vowel:
                maxi += 1          # Increment the current consecutive vowel count.

            # Check if the window size (k) is reached and the character at the beginning of the window is a vowel.
            if i >= k and s[i - k] in kVowels:
                maxi -= 1          # Decrement the current consecutive vowel count, as it's moving out of the window.

            ans = max(ans, maxi)  # Update the maximum count of consecutive vowels.

        return ans  # Return the maximum count of consecutive vowels in any window of size 'k'.

#392. Is Subsequence

class Solution:
    def isSubsequence(self, s, t):
        # Check if the length of 's' is greater than 't'
        if len(s) > len(t):
            return False
        # If 's' is empty, it's always a subsequence of 't'
        if len(s) == 0:
            return True
        
        subsequence = 0
        # Loop through each character in 't'
        for i in range(0, len(t)):
            # Check if 'subsequence' index is within bounds of 's'
            if subsequence <= len(s) - 1:
                # Print the current character in 's' being checked
                print(s[subsequence])
                # If the current character in 's' matches the character in 't'
                if s[subsequence] == t[i]:
                    subsequence += 1  # Move to the next character in 's'
        
        # Check if the entire 's' has been traversed as a subsequence
        return subsequence == len(s)

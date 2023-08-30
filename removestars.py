#2390. Removing Stars From a String

class Solution:
    def removeStars(self, s):
        ans = []  # Initialize an empty list to store the characters
        for c in s:
            if c == '*':  # Check if the character is a '*'
                ans.pop()  # Remove the last character from the list
            else:
                ans.append(c)  # Append the character to the list if it's not '*'
        return ''.join(ans)  # Join the characters in the list to form a string

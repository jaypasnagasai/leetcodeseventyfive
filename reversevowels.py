class Solution:
    def reverseVowels(self, s):
        # Convert the input string into a list of characters for easy manipulation
        chars = list(s)
        
        # Set of vowels (both lowercase and uppercase)
        kVowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        # Initialize pointers for the left and right ends of the string
        l = 0
        r = len(s) - 1
        
        # Continue swapping characters until the left pointer is less than the right pointer
        while l < r:
            # Move the left pointer to the right until a vowel is found
            while l < r and chars[l] not in kVowels:
                l += 1
            
            # Move the right pointer to the left until a vowel is found
            while l < r and chars[r] not in kVowels:
                r -= 1
            
            # Swap the vowels found by the left and right pointers
            chars[l], chars[r] = chars[r], chars[l]
            
            # Move the pointers towards each other for the next iteration
            l += 1
            r -= 1
        
        # Convert the list of characters back into a string and return
        return ''.join(chars)

# 1071. Greatest Common Divisor of Strings

class Solution:
  def gcdOfStrings(self, str1, str2):
    def mod(s1, s2):
      while s1.startswith(s2):
        s1 = s1[len(s2):]  # Remove s2 from the beginning of s1
      return s1

    if len(str1) < len(str2):
      return self.gcdOfStrings(str2, str1)  # Swap str1 and str2 if str1 is shorter
    if not str1.startswith(str2):
      return ''  # If str1 doesn't start with str2, no common divisor
    if not str2:
      return str1  # If str2 is empty, str1 is the common divisor
    return self.gcdOfStrings(str2, mod(str1, str2))  # Recursively find GCD

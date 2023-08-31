#17. Letter Combinations of a Phone Number

class Solution:
  def letterCombinations(self, digits):
    if not digits:
      return []

    digitToLetters = ['', '', 'abc', 'def', 'ghi',
                      'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ans = []

    def dfs(i, path):
      if i == len(digits):
        ans.append(''.join(path))
        return

      for letter in digitToLetters[ord(digits[i]) - ord('0')]:
        path.append(letter)
        dfs(i + 1, path)
        path.pop()

    dfs(0, [])
    return ans

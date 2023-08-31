#216. Combination Sum III

class Solution:
  def combinationSum3(self, k, n):
    ans = []

    def dfs(k, n, s, path):
      if k == 0 and n == 0:
        ans.append(path)
        return
      if k == 0 or n < 0:
        return

      for i in range(s, 10):
        dfs(k - 1, n - i, i + 1, path + [i])

    dfs(k, n, 1, [])
    return ans

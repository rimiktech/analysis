#Program to find length of longest palindromic subsequence in Python
class Solution:
   def solve(self, s):
      n = len(s)
      def dp(i, j):
         if i == j:
            return 1
         elif i > j:
            return 0
         else:
            if s[i] == s[j]:
               return 2 + dp(i + 1, j - 1)
            else:
               return max(dp(i + 1, j), dp(i, j - 1))
      return dp(0, n - 1)
ob = Solution()
s = "hfkjlklyghfdri"
print(ob.solve(s))

            

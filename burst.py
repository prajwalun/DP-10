# The maxCoins method calculates the maximum coins that can be collected by bursting balloons optimally.

# Dynamic Programming Approach:
# - Add 1 to both ends of the array to handle edge cases.
# - Use a 2D `dp` array where `dp[l][r]` stores the maximum coins obtainable from indices `l` to `r`.
# - Iterate over subarray lengths:
#   - For each subarray, consider every possible balloon to burst last.
#   - Calculate the coins from bursting that balloon and add the maximum coins from left and right subarrays.
#   - Update `dp[l][r]` with the maximum value.

# TC: O(n^3) - Three nested loops: length, left, and bursting balloon.
# SC: O(n^2) - Space for the `dp` array.



class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]
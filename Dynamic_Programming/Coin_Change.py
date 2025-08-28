class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Creates an array for tabulation
        dp = [amount + 1] * (amount + 1)
        # Initializes the first value to 0
        dp[0] = 0

        # Loops for all possible values up to amount
        for a in range(1, amount + 1):
            # Loops through each coin amount 
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        # Checks if dp[amount] ever got changed
        return dp[amount] if dp[amount] != amount + 1 else -1
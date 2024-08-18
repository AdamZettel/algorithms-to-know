def coin_change_min_coins(coins, amount):
    """Dynamic Programming approach to find the minimum number of coins."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for x in range(1, amount + 1):
        for coin in coins:
            if x >= coin:
                dp[x] = min(dp[x], dp[x - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_num_ways(coins, amount):
    """Dynamic Programming approach to find the number of ways to make the amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    
    return dp[amount]

# Example usage:
coins = [1, 2, 5]
amount = 11

# Find the minimum number of coins required
min_coins = coin_change_min_coins(coins, amount)
print(f"Minimum number of coins: {min_coins}")  # Output: 3

# Find the number of ways to make the amount
num_ways = coin_change_num_ways(coins, amount)
print(f"Number of ways to make the amount: {num_ways}")  # Output: 11

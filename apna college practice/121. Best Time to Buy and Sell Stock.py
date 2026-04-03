def maxProfit(prices):
    n = len(prices)
    min_prices = prices[0]
    max_profit = 0

    for i in range(1, n):
        if prices[i] < min_prices:
            min_prices = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_prices)

    return max_profit


# VS Code run
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
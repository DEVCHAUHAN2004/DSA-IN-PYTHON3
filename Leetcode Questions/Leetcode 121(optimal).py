def stock_buy_sell(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)

    return max_profit

prices = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(prices))





# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         n = len(prices)
#         max_profit = 0
#         min_price = float("inf")  # should be positive infinity

#         for i in range(n):
#             min_price = min(min_price, prices[i])
#             profit = prices[i] - min_price
#             max_profit = max(max_profit, profit)

#         return max_profit

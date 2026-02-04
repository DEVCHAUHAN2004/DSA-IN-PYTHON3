prices = [7,2,1,5,6,4,8]

# def stock_buy_sell(nums):
#   n = len(nums)
#   x = max(nums)
#   y = min(nums)
#   z = x-y
#   return z
# print(stock_buy_sell(nums))
# # 7

def stock_buy_sell(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
    return max_profit

# prices = [7, 1, 5, 3, 6, 4]
print(stock_buy_sell(prices))
# 7




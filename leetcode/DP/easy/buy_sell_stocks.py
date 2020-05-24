"""
121. Best Time to Buy and Sell Stock
"""

def stocks(prices):
    min_pri, max_pro = prices[0], 0
    for i in range(1, len(prices)):
        min_pri = min(min_pri, prices[i])
        max_pro = max(max_pro, prices[i] - min_pri)
    return max_pro

def stocks_kadane(prices):
    max_cur, max_sofar = 0, 0
    for i in range(1, len(prices)):
        max_cur = max(0, max_cur + prices[i] - prices[i-1])
        max_sofar = max(max_sofar, max_cur)
    return max_sofar

print stocks([7,1,5,3,6,4])
print stocks_kadane([7,1,5,3,6,4])

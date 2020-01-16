"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
            Not 7-1 = 6, as selling price needs to be larger than buying price.
"""

"""Commentary

This question tests your ability to use a greedy algorithm correctly and more importantly to recognize that
the optimal solution is to use a greedy approach.

In this case, we want the largest profit which means we ideally want to sell at the highest price and buy at the lowest price.
Knowing this, we can reason about a greedy algorithm to solve this question.

If we do a greedy approach it most likely solves the problem in one pass. Thus we at least need a counter for
the max profit so far. As we iterate through each day, we notice that can calculate a potential profit on that day
by subtracting that day's price from the minimum price that we bought our stock. That is the key to this problem. We
need to know the minimum price so far. In this case, let's set it to the first day and then calculate the first potential
profit on day two and then just iterate through the rest of the days. Through each day, we update both the max profit compared to that
days potential profit and then the minimum price. This order of checking our counters is required because we calculate
our potential profit based on the minimum price before we make the update.
"""


def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for price_index in range(1, len(prices)):
        current_price = prices[price_index]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)

    if max_profit < 0:
        return 0
    return max_profit

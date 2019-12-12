def calculate_max_profit(prices):
    if len(prices) < 2:
        raise ValueError("The list of prices must have at least two prices.")

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for time in range(1, len(prices)):
        current_price = prices[time]
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit

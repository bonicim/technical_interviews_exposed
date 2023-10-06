def calculate_max_profit(prices):
    return calculate_max_profit_efficient(prices)


def calculate_max_profit_naive(prices: list[int]):
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


def calculate_max_profit_efficient(prices: list[int]):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        current_profit = prices[right] - prices[left]
        max_profit = max(max_profit, current_profit)

        if prices[left] > prices[right]:
            left = right

        right += 1

    return max_profit

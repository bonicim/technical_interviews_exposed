def coin_change(coins, amount):
    return coin_change_top_down(coins, amount)


def coin_change_top_down(coins, amount):
    def coin_change(coins, amount, balance, cache):
        if balance < 0:
            return -1

        if balance == 0:
            return 0

        # we already have an answer for the minimum number of coins for the balance
        if cache[balance] != 0:
            return cache[balance]

        # we go here if we don't have a cached answer. Thus, we calculate it by testing each coin denomination
        min_coins = amount + 1
        for coin in coins:
            count_coins_to_use = coin_change(coins, amount, balance - coin, cache)
            # update the min_coins needed if we can use less coins
            if count_coins_to_use >= 0 and count_coins_to_use < min_coins:
                min_coins = count_coins_to_use + 1

        if min_coins == amount + 1:
            cache[balance] = -1
        else:
            cache[balance] = min_coins

        return cache[balance]

    if amount < 1:
        return 0

    cache = [0] * (amount + 1)
    return coin_change(coins, amount, amount, cache)


def coin_change_bottom_up(coins, amount):
    cache = [amount + 1] * (amount + 1)
    cache[0] = 0

    for subamount in range(1, amount + 1):
        for _, coin in enumerate(coins):
            # only consider recalculate the minimum coins needed for a subamount if the given coin is less than or equal to the subamount
            if coin <= subamount:
                remaining_balance = subamount - coin
                cache[subamount] = min(cache[subamount], 1 + cache[remaining_balance])

    if cache[amount] > amount:
        return -1
    return cache[amount]

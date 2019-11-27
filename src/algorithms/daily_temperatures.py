def get_days_to_warmer_temp(temperatures):
    """
    Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

    For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

    def next_future_day_temp():
        return increasing_temps_stack[-1][1]

    def next_future_day_index():
        return increasing_temps_stack[-1][0]

    days_till_increase = [0] * len(temperatures)
    increasing_temps_stack = []

    for index in range(len(temperatures) - 1, -1, -1):
        current_temp = temperatures[index]

        while increasing_temps_stack and current_temp >= next_future_day_temp():
            increasing_temps_stack.pop()
        if increasing_temps_stack:
            days_till_increase[index] = next_future_day_index() - index

        increasing_temps_stack.append((index, current_temp))

    return days_till_increase

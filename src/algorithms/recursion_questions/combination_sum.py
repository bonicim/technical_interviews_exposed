def combination_sum(choices, target):
    result = []
    recursion(choices, target, result, [])
    return result


def recursion(choices, remaining, result, combo):
    if remaining == 0:
        combo = sorted(combo)
        if combo not in result:
            result.append(combo)
            return result

    for choice in choices:
        if choice <= remaining:
            remaining_at_this_choice = remaining - choice
            temp_combo = combo.copy()
            temp_combo.append(choice)
            recursion(choices, remaining_at_this_choice, result, temp_combo)

def find_grants_cap(grants_array, new_budget):
    return solution_v1(grants_array, new_budget)


def solution_v1(grants_array, new_budget):
    if sum(grants_array) <= new_budget:
        return max(grants_array)

    grants_array = sorted(grants_array)
    grants_remaining = len(grants_array)
    current_cap = new_budget / grants_remaining

    for grant in grants_array:
        if grant <= current_cap:
            grants_remaining -= 1
            new_budget -= grant
            current_cap = new_budget / grants_remaining
        else:
            return current_cap

    return current_cap

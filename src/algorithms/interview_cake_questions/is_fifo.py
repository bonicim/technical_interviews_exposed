def is_fifo(takeout, dine_in, served):
    # return is_fifo_iterative(takeout, dine_in, served)
    # return is_fifo_recursive_v2(takeout, dine_in, served)
    return is_fifo_recursive(takeout, dine_in, served)


def is_fifo_recursive(takeout, dine_in, served):
    # this is an expensive implementation costing us time and space of n^2; do you know why?
    # is_fifo_recursive_v2 is optimized for time at a cost of n
    if not served and not takeout and not dine_in:
        return True
    elif not served and (takeout or dine_in):
        return False
    elif takeout and served[0] == takeout[0]:
        return is_fifo_recursive(takeout[1:], dine_in, served[1:])
    elif dine_in and served[0] == dine_in[0]:
        return is_fifo_recursive(takeout, dine_in[1:], served[1:])
    else:
        return False


def is_fifo_recursive_v2(takeout, dine_in, served):
    return is_fifo_recursive_v2_helper(takeout, dine_in, served, 0, 0, 0)


def is_fifo_recursive_v2_helper(
    takeout, dine_in, served, takeout_index, dine_in_index, served_index
):
    if (
        served_index == len(served)
        and takeout_index == len(takeout)
        and dine_in_index == len(dine_in)
    ):
        return True
    elif served_index == len(served) and (
        takeout_index < len(takeout) or dine_in_index < len(dine_in)
    ):
        return False
    elif (
        takeout_index < len(takeout) and served[served_index] == takeout[takeout_index]
    ):
        return is_fifo_recursive_v2_helper(
            takeout, dine_in, served, takeout_index + 1, dine_in_index, served_index + 1
        )
    elif (
        dine_in_index < len(dine_in) and served[served_index] == dine_in[dine_in_index]
    ):
        return is_fifo_recursive_v2_helper(
            takeout, dine_in, served, takeout_index, dine_in_index + 1, served_index + 1
        )
    else:
        return False


def is_fifo_iterative(takeout, dine_in, served):
    takeout_order = list(takeout)
    dine_in_order = list(dine_in)
    served_order = list(served)

    for order in served_order:
        if takeout_order and order == takeout_order[0]:
            takeout_order.pop(0)
        elif dine_in_order and order == dine_in_order[0]:
            dine_in_order.pop(0)
        else:
            return False

    if takeout_order or dine_in_order:
        return False

    return True

def is_fifo(takeout, dine_in, served):
    """
    My cake shop is so popular, I'm adding some tables and hiring wait staff so folks can have a cute sit-down cake-eating experience.

    I have two registers: one for take-out orders, and the other for the other folks eating inside the cafe. All the customer orders get combined into one list for the kitchen, where they should be handled first-come, first-served.

    Recently, some customers have been complaining that people who placed orders after them are getting their food first. Yikes—that's not good for business!

    To investigate their claims, one afternoon I sat behind the registers with my laptop and recorded:

    The take-out orders as they were entered into the system and given to the kitchen. (take_out_orders)
    The dine-in orders as they were entered into the system and given to the kitchen. (dine_in_orders)
    Each customer order (from either register) as it was finished by the kitchen. (served_orders)
    Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

    We'll represent each customer order as a unique integer.

    As an example,

    Take Out Orders: [1, 3, 5]
    Dine In Orders: [2, 4, 6]
    Served Orders: [1, 2, 4, 6, 5, 3]
    would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

    But,

    Take Out Orders: [1, 3, 5]
    Dine In Orders: [2, 4, 6]
    Served Orders: [1, 2, 3, 5, 4, 6]
    would be first-come, first-served.
    """
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
        takeout_index < len(takeout) and takeout[takeout_index] == served[served_index]
    ):
        return is_fifo_recursive_v2_helper(
            takeout, dine_in, served, takeout_index + 1, dine_in_index, served_index + 1
        )
    elif (
        dine_in_index < len(dine_in) and dine_in[dine_in_index] == served[served_index]
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

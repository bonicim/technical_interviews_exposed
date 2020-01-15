def merge_sorted_lists(list1, list2):
    """
    In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

    Each order is represented by an "order id" (an integer).

    We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

    For example:

    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print(merge_lists(my_list, alices_list))
    """

    """Commentary
    Similar to the merge sorted linked list, this problem tests your ability to handle while loops and index out of bound
    errors. The key idea is to check that the index of either list is not out-of-bounds as we traverse the length of the merged array.
    We are guaranteed to traverse the combined length of both list because we have to visit each box of each list at most one time.


    """

    merged = [0] * (len(list1) + len(list2))
    curr_index_list1 = 0
    curr_index_list2 = 0

    for merged_index in range(len(merged)):
        list1_empty = curr_index_list1 >= len(list1)
        list2_empty = curr_index_list2 >= len(list2)

        if list1_empty and not list2_empty:
            merged[merged_index] = list2[curr_index_list2]
            curr_index_list2 += 1
        elif list2_empty and not list1_empty:
            merged[merged_index] = list1[curr_index_list1]
            curr_index_list1 += 1
        elif list1[curr_index_list1] < list2[curr_index_list2]:
            merged[merged_index] = list1[curr_index_list1]
            curr_index_list1 += 1
        else:
            merged[merged_index] = list2[curr_index_list2]
            curr_index_list2 += 1

    return merged

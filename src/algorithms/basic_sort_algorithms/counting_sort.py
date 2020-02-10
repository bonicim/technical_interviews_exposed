from collections import Counter


def counting_sort(arr_of_ints):
    # generate a frequency table of ints
    freqs = Counter(arr_of_ints)
    highest_freq = freqs.most_common(1) + 1
    buckets = [0] * highest_freq

    # use indexes as keys and the value as the frequency of the index, which is the integer in the array of ints input
    for num in arr_of_ints:
        buckets[num] += 1

    # create modified frequency list by adding previous counts to the current count of the number, sort of like an accumulating function
    output = [0] * len(arr_of_ints)
    output[0] = buckets[0]
    for index in range(1, len(output)):
        output[index] = output[index - 1] + buckets[index]

    # a sorted permutation of the input array such that output[0] <= output[1] <= output[len(input) - 1]
    return output

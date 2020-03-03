def three_sum(nums):
    def two_sum_to_zero(index, nums, target):
        triplets = []
        complements = set()

        while index < len(nums):
            num2 = nums[index]
            complement = -target - num2

            if complement in complements:
                triplets.append([target, num2, complement])

                while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                    index += 1

            complements.add(num2)
            index += 1

        return triplets

    triplets = []
    sorted_nums = sorted(nums)

    for index, num in enumerate(sorted_nums):
        if index == 0 or (sorted_nums[index] != sorted_nums[index - 1]):
            new_triplets = two_sum_to_zero(index + 1, sorted_nums, num)
            for triplet in new_triplets:
                triplets.append(triplet)
    return triplets


def two_pointers(nums):
    triplets = []
    # the solution relies on a sorted list because it uses the sorted property to avoid duplicates and correctly calculate the total sum
    sorted_nums = sorted(nums)

    for index, num in enumerate(sorted_nums):
        # only compare if num is the first one or the element is not a duplicate
        if index == 0 or sorted_nums[index] != sorted_nums[index - 1]:
            left = index + 1
            right = len(sorted_nums) - 1

            while left < right:
                left_num = sorted_nums[left]
                right_num = sorted_nums[right]

                if num + left_num + right_num == 0:
                    triplets.append([num, left_num, right_num])
                    left += 1
                    # skip the duplicates
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1
                elif num + left_num + right_num < 0:
                    left += 1
                else:
                    right -= 1

    return triplets

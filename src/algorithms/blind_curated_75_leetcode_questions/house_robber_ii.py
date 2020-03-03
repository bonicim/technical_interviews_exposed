def rob(nums):
    def rob_circle(nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        cache = [0] * (len(nums))

        cache[0] = nums[0]
        cache[1] = max(nums[1], cache[0])

        for index in range(2, len(nums)):
            cache[index] = max(nums[index] + cache[index - 2], cache[index - 1])

        return cache[len(nums) - 1]

    if not nums:
        return 0

    if len(nums) <= 3:
        return max(nums)

    amount_with_first_house = rob_circle(nums[: len(nums) - 1])
    amount_with_last_house = rob_circle(nums[1:])
    return max(amount_with_first_house, amount_with_last_house)

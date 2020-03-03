def top_k_frequent(nums, k):
    counter = dict()

    for num in nums:
        count = counter.get(num, 0)
        count += 1
        counter.update({num: count})

    buckets = [[] for _ in range(len(nums) + 1)]
    for key, val in counter.items():
        bucket = buckets[val]
        bucket.append(key)
        buckets[val] = bucket

    res = []
    for bucket in buckets[::-1]:
        for num in bucket:
            if len(res) == k:
                return res
            res.append(num)
    return res

movies = [90, 85, 75, 60, 120, 150, 125]
d = 250


def twoSumClosest(nums, target):

    target = target - 30

    nums = sorted(nums)

    lo, hi = 0, len(nums) - 1

    minDiff = float('inf')

    # we greedily decrease when we have too, and increase lo as much as possible
    while lo < hi:

        # We may be able to bring lo up

        if nums[lo] + nums[hi] > target:
            hi -= 1
        elif nums[lo] + nums[hi] < target:

            if target - nums[lo] + nums[hi] < minDiff:
                minDiff = target - nums[lo] + nums[hi]
                result = lo, hi

            lo += 1
        else:
            result = lo, hi

    return nums[result[0]], nums[result[1]]


print(twoSumClosest(movies, d))

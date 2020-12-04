def twoSumExact(nums, target):
    want = {}
    # max number in a feasible answer
    maxNum = -1

    for num in nums:
        want[target - num] = num

        # feasible
        if num in want:
            # optimal
            largestInSol = max(num, want[num])
            if largestInSol > maxNum:
                maxNum = largestInSol

    return (maxNum, target-maxNum)


print(twoSumExact([20, 50, 40, 25, 30, 10], 60))

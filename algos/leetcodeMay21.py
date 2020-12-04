def maxDotProduct(nums1, nums2) -> int:
    n = len(nums1)
    m = len(nums2)
    maxLength = min(n, m)

    r = -90999999999999

    dp = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(maxLength)]
    for l in range(1, maxLength+1):
        print(l)


nums1 = [2, 1, -2, 5]
nums2 = [3, 0, -6]
r = maxDotProduct(nums1, nums2)
# 18
print(r)

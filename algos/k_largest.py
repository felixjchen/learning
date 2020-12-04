
import heapq


def k_largest(A, k):
    print(A)
    heapq._heapify_max(A)
    print(A)

    return [heapq._heappop_max(A) for _ in range(k)]
    # return heapq.nlargest(k, A)


print(k_largest([4, 5, 6, 7, 8, 1, 2, 3, 4], 3))

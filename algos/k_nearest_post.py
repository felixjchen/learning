import heapq
from math import sqrt

you = [0, 0]
post_offices = [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3


def euclidianDistance(p1, p2):
    p1ToP2 = [p2[0] - p1[0], p2[1] - p1[1]]
    return sqrt(p1ToP2[0] ** 2 + p1ToP2[1] ** 2)

# O(klogn) which will be not worse then O(nlogn)


def k_closest_post_offices(k, you, post_offices):
    H = []

    # O(n)
    for i in post_offices:
        H.append((euclidianDistance(you, i), i))

    # O(n)
    heapq.heapify(H)

    # (klogn)
    return [heapq.heappop(H)[1] for i in range(k)]


print(k_closest_post_offices(k, you, post_offices))

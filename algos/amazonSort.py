truckSpace = 90
packagesSpace = [1, 10, 25, 35, 60]


def amazonSort(truckSpace, packagesSpace):

    if truckSpace < 30:
        return [-1, -1]

    truckSpace -= 30
    lo, hi = 0, len(packagesSpace) - 1

    bestDiff = float('inf')
    bestLo, bestHi = -1, -1

    while lo < hi:
        diff = truckSpace - (packagesSpace[lo] + packagesSpace[hi])

        if diff < 0:
            hi -= 1

        elif diff > 0:
            if diff < bestDiff:
                bestLo, bestHi = lo, hi
            lo += 1

        else:
            bestLo, bestHi = lo, hi
            break

    print(bestLo, bestHi)

    return bestLo, bestHi


amazonSort(truckSpace, packagesSpace)

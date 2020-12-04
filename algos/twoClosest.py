movies = [90, 85, 75, 60, 120, 150, 125]
target = 250


def twoClosest(a, target):

    target -= 30

    i, j = 0, len(a) - 1

    minDiff = float('inf')
    result = (None, None)

    while i < j:
        diff = target - (a[i] + a[j])

        if diff < 0:
            j -= 1
        else:
            if diff < minDiff:
                minDiff = diff
                result = a[i], a[j]
            i += 1

    return result


print(twoClosest(movies, target))

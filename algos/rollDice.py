pipsPerDice = 6

def cost(dice):
    pipCount = [0] * pipsPerDice

    # Get all dice states, O(n)
    for i in dice:
        pipCount[i-1] += 1

    print(pipCount)

    minCost = float("inf")
    # O(1)
    for i in range(0, pipsPerDice):

        # opposite side of the dice has highest cost, x2 cost
        oppositeSide = pipsPerDice - i - 1

        # We move all pips once if not on goal, once more if on oppositeSide
        cost = (sum(pipCount) - pipCount[i]) + pipCount[oppositeSide] 

        # Follow min
        if cost < minCost: minCost = cost

    # print(cost)
    return minCost

dice = [1, 6, 2, 3]
print(cost(dice))
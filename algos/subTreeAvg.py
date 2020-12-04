class Node:
    def __init__(self, value, children = []):
        self.value = value
        self.children = children

child1 = Node(-5, children=[Node(1), Node(2)])
child2 = Node(13, children=[Node(4), Node(-2)])
child3= Node(4)
root = Node(1, children=[child1, child2, child3])

def maxAvgSubtree(root):
    def getValue(root):
        return root.value + sum([getValue(i) for i in root.children])
    def getCount(root):
        return 1 + sum([getCount(i) for i in root.children])

    return max([getValue(i)/getCount(i) for i in root.children])

print(maxAvgSubtree(root))
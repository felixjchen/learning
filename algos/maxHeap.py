class maxHeap():
    def __init__(self):
        self._heap = []

    def peak(self):
        if not self._heap:
            return -1
        return self._heap[0]

    def insert(self, item):
        self._heap.append(item)

        parentPos = len(self._heap) // 2
        # print(parentPos)

        while max(self._heap[parentPos - 1], self._heap[parentPos * 2 - 1], self._heap[parentPos * 2]) != self._heap[parentPos - 1]:
            # print(self._heap)
            # print(parentPos)

            parentEle = self._heap[parentPos - 1]
            rightEle = self._heap[parentPos*2]
            leftEle = self._heap[parentPos*2 - 1]

            if parentEle < rightEle:
                self._heap[parentPos - 1], self._heap[parentPos *
                                                      2] = self._heap[parentPos*2], self._heap[parentPos - 1]
            elif parentEle < leftEle:
                self._heap[parentPos - 1], self._heap[parentPos*2 -
                                                      1] = self._heap[parentPos*2-1], self._heap[parentPos - 1]

            # up
            parentPos = parentPos // 2


h = maxHeap()
h.insert(6)
h.insert(5)

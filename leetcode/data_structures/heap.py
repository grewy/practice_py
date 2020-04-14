

class Heap(object):

    def __init__(self, arr):
        self.heap = arr
        self.heapify()

    def _shift_up(self, idx):

        while idx > 0:
            i = idx // 2
            if self.heap[i] < self.heap[idx]:
                self.heap[i], self.heap[idx] = self.heap[idx], self.heap[i]
            idx = i

    def heapify(self):
        last_idx = len(self.heap) - 1

        while last_idx >= 0:
            self._shift_up(last_idx)
            last_idx -= 1

import sys
h = Heap(sys.argv[1][1:-1].split(','))
print h.heap

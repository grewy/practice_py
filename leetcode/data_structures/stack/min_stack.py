class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = 99999999
        self._list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self._list.append(x)
        if len(self._list) == 1:
            self._min = x
        else:
            self._min = min(self._min, x)


    def pop(self):
        """
        :rtype: None
        """
        _x = self._list.pop()
        if len(self._list) > 0:
            self._min = min(self._list)
        if len(self._list) == 0:
            self._min = _x

    def top(self):
        """
        :rtype: int
        """
        if self._list:
            return self._list[-1]
        else:
            return

    def getMin(self):
        """
        :rtype: int
        """
        return self._min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

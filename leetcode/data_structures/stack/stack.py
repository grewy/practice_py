class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._stack = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self._stack.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self._stack) > 0:
            return self._stack.pop(-1)
        else:
            return -1


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self._stack) > 0:
            return self._stack[-1]
        else:
            return -1


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self._stack) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

import unittest

class StackEmptyError(Exception):
    pass

class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, val):
        self._stack.append(val)

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("StackEmptyError")
        return self._stack.pop(-1)

    def top(self):
        if self.is_empty():
            raise StackEmptyError("StackEmptyError")
        return self._stack[-1]

    def is_empty(self):
        return (len(self._stack) == 0)


class MinStack(object):
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()

    def push(self, val):
        self.stack.push(val)
        try:
            _min = self.get_min()
        except StackEmptyError:
            self.min_stack.push(val)
            return True
        if val < _min:
            self.min_stack.push(val)
        return True

    def pop(self):
        poped_item = self.stack.pop()
        if poped_item == self.get_min():
            self.min_stack.pop()
        return poped_item

    def top(self):
        return self.stack.top()

    def get_min(self):
        return self.min_stack.top()

    def is_empty(self):
        return self.stack.is_empty()



class TestMinStack(unittest.TestCase):
    def setUp(self):
        self.st = MinStack()

    def test_empty_pop(self):
        with self.assertRaises(StackEmptyError) as ctx:
             self.st.pop()
        self.assertEqual("StackEmptyError", str(ctx.exception))

    def test_empty_top(self):
        with self.assertRaises(StackEmptyError) as ctx:
            self.st.top()
        self.assertEqual("StackEmptyError", str(ctx.exception))

    def test_push_pop(self):
        self.st.push(10)
        self.st.push(-1)
        self.st.push(20)
        self.st.push(0)
        self.st.push(-2)
        self.assertEqual(-2, self.st.get_min())
        self.st.pop()
        self.assertEqual(-1, self.st.get_min())
        self.st.pop()
        self.st.pop()
        self.st.pop()
        self.assertEqual(10, self.st.get_min())
        self.st.pop()
        self.assertEqual(True, self.st.is_empty())

if __name__ == '__main__':
    unittest.main()

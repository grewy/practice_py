class Stack(object):
    def __init__(self):
        self.items = []
        self.size = len(self.items)

    def get_size(self):
        return self.size

    def push(self, item):
        if self.get_size() == 0:
            self.items.append((item, item))
        elif self.get_size() > 0:
            _min = self.peek()[1] if self.peek()[1] < item else item
            self.items.append((item, _min))
        self.size += 1

    def pop(self):
        if self.get_size() > 0:
            self.size -= 1
            return self.items.pop(-1)

    def peek(self):
        if self.get_size() > 0:
            return self.items[-1]

    def get_min(self):
        if self.get_size() > 0:
            return self.peek()[1]



import unittest


class TestStack(unittest.TestCase):
    def setUp(self):
        self.st = Stack()

    def test_empty_pop(self):
        self.assertEqual(self.st.pop(), None)

    def test_empty_get_min(self):
        self.assertEqual(self.st.get_min(), None)

    def test_insert_empty(self):
        self.st.push(10)
        self.assertEqual(self.st.get_size(), 1)
        self.assertEqual(self.st.pop(), (10, 10))

    def test_get_min(self):
        self.st.push(1)
        self.st.push(10)
        self.st.push(-2)
        self.st.push(-1000)
        self.assertEqual(self.st.get_min(), -1000)
        self.st.pop()
        self.st.push(1000)
        self.st.pop()
        self.assertEqual(self.st.get_min(), -2)



if __name__ == '__main__':
    unittest.main()

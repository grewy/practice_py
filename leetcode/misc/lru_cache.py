import collections

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.d = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.d:
            return -1
        value = self.d.pop(key)
        self.d[key] = value
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.d.get(key):
            self.d.pop(key)
            self.d[key] = value
        else:
            if self.capacity > 0:
                self.capacity -= 1
                self.d[key] = value
            elif self.capacity == 0:
                self.d.popitem(last=False)
                self.d[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

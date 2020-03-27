class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def iter_str(st):
            skip = 0
            for x in st[::-1]:
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x,y in itertools.izip_longest(iter_str(S), iter_str(T)))

CHAR_SIZE = 26

class Trie(object):

    def __init__(self):
        self.is_leaf = False
        self.children = [None]*CHAR_SIZE

    def insert(self, key):
        print "inserting... %s" % key

        cur = self
        for c in key:
            idx = ord(c) - ord('a')
            if cur.children[idx] is None:
                cur.children[idx] = Trie()
            cur = cur.children[idx]

        cur.is_leaf = True

    def search(self, key):
        print "searching.....%s" % key

        cur= self
        for c in key:
            idx = ord(c) - ord('a')
            cur = cur.children[idx]
            if cur is None:
                return False
        return cur.is_leaf



if __name__ == '__main__':
    head = Trie()
    head.insert('xyz')
    print head.search('xyz')
    print head.search('xy')
    print head.search('xyzs')

import unittest
import time


def Match(s, p, n, m):
    if n < 0 and m < 0:
        return True

    if m < 0:
        return False

    if n < 0:
        if all(x == '*' for x in p[:m]):
            return True
        return False

    if p[m] == '*':
        return Match(s, p, n -1, m) or Match(s, p, n, m - 1)

    elif p[m] == '?':
        return Match(s, p, n -1, m-1)

    else:
        if p[m] != s[n]:
            return False
        else:
            return Match(s, p, n-1, m-1)


class TestMatch(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.6f' % (self.id(), t))

    def test_stars_match(self):
        f = Match("xyxzzxy", "x*y", 6, 2)
        self.assertEqual(True, f)

    def test_stars_nomatch(self):
        f = Match("xyxzzxy", "x*x", 6, 2)
        self.assertEqual(False, f)

    def test_stars_question_match(self):
         f = Match("xyxzzxy", "x*******x?", 6, 9)
         self.assertEqual(True, f)

    def test_only_star_match(self):
          f = Match("xyxzzxy", "**", 6, 1)
          self.assertEqual(True, f)

if __name__ == '__main__':
    unittest.main()

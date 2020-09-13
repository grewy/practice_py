import unittest
import time

def Match(s, p, n, m, lookup):
    if n < 0 and m < 0:
        return True

    if m < 0:
        return False

    if n < 0:
        if all(x == '*' for x in p[:m]):
            return True
        return False

    if not lookup[n][m]:
      if p[m] == '*':
          return Match(s, p, n -1, m, lookup) or Match(s, p, n, m - 1, lookup)

      elif p[m] == '?':
          return Match(s, p, n -1, m-1, lookup)

      else:
          if p[m] != s[n]:
              return False
          else:
              return Match(s, p, n-1, m-1, lookup)
    return lookup[n][m]

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.6f' % (self.id(), t))

    def test_stars_match(self):
        s = "xyxzzxy"
        p = "x*y"
        lookup = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1) ]
        f = Match(s, p, len(s) - 1, len(p) - 1, lookup)
        self.assertEqual(True, f)

    def test_stars_nomatch(self):
        s = "xyxzzxy"
        p = "x*x"
        lookup = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1) ]
        f = Match(s, p, len(s) - 1, len(p) - 1, lookup)
        self.assertEqual(False, f)

    def test_stars_question_match(self):
        s = "xyxzzxy"
        p = "x*******x?"
        lookup = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1) ]
        f = Match(s, p, len(s) - 1, len(p) - 1, lookup)
        self.assertEqual(True, f)

    def test_only_star_match(self):
        s = "xyxzzxy"
        p = "*"
        lookup = [[False for _ in range(len(p) + 1)] for _ in range(len(s)+1) ]
        f = Match(s, p, len(s) - 1, len(p) - 1, lookup)
        self.assertEqual(True, f)

if __name__ == '__main__':
    unittest.main()

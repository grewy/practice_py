def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        rows = {}
        cols = {}
        count = 0

        mat = []

        for r, c in indices:
            rows[r] = rows.get(r, 0) + 1
            cols[c] =cols.get(c, 0) + 1


        for r in range(n):
            mat.append([0]*m)

        for k, v in rows.iteritems():
            mat[k] = [v]*m


        for r in range(n):
            for c, v in cols.iteritems():
                mat[r][c] += v
            count += sum(1 for x in mat[r] if x % 2 != 0)


        return count

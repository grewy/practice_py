def generate(self, rows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        al = []
        def fact(n):
            res=1
            for c in range(1,n+1):
                res = res*c
            return res


        for i in range(0, rows):
            a=[]
            for k in range(0, i+1):
                coff = int(fact(i)/(fact(k)*fact(i-k)))
                a.append(coff)
            al.append(a)

        return al

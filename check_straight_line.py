def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        INFI = 10000000000
        if len(coordinates) < 2:
            return False

        upper = coordinates[-1]
        lower = coordinates[0]

        yaxis = upper[1] -lower[1]
        xaxis = float(upper[0] - lower[0])
        slope = abs(yaxis/xaxis) if xaxis != 0 else INFI

        for upper in coordinates[2:]:
            yaxis = upper[1] -lower[1]
            xaxis = float(upper[0] - lower[0])
            _slope = abs(yaxis/xaxis) if xaxis != 0 else INFI
            if  _slope != slope:
                return False
        return True

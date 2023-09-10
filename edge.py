from math import sin, cos, sqrt, atan2, radians


class Edge:
    def __init__(self, end_p1, end_p2):
        self.end_p1 = end_p1
        self.end_p2 = end_p2
        self.weight = self.calc_weight()


    def calc_weight(self):
        R = 6373.0
        dlong =  radians(self.end_p2.long) - radians(self.end_p1.long)
        dlat = radians(self.end_p2.lat) - radians(self.end_p1.lat)
        a = sin(dlat / 2)**2 + (cos(self.end_p1.lat) * cos(self.end_p2.lat) * sin(dlong / 2)**2)
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return round(distance, 3)


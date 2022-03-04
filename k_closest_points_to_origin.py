class Solution:
    def kClosest(self, points, k: int):
        points.sort(key = self.distance)
        return points[:k]
    
    def distance(self, point):
        return point[0]**2+point[1]**2
        
#Write a function "minTimeToVisit" to find the minimum time in 
# the visit all points.
class Solution:
    def minTimeToVisit(points):
        if not points:
            return 0
        result = 0
        for i in range(1, len(points)):
            result += max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
        return result


points = [[-1,2],[3,-4],[5,-6]]
print(Solution.minTimeToVisit(points))
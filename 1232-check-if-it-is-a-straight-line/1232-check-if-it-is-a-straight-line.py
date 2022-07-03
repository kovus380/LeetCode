class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x_points = [x_point for x_point, y_point in coordinates]
        y_points = [y_point for x_point, y_point in coordinates]
        x_points_set, y_points_set = list(set(x_points)), list(set(y_points))
        if len(x_points_set) == 1:
            return True
        if len(x_points_set) != len(x_points):
            return False
        slope = (coordinates[-1][1] - coordinates[0][1]) // (coordinates[-1][0] - coordinates[0][0])
        for i in range(len(coordinates) - 1):
            if (coordinates[i + 1][1] - coordinates[i][1]) // (coordinates[i + 1][0] - coordinates[i][0]) != slope:
                return False
        return True
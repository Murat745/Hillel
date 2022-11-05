"""
Lesson 14, homework 10, task 2 solution.
Circle and Point classes. 
"""


class Point:
    def __init__(self, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position


class Circle:
    def __init__(self, center_x_position, center_y_position, radius):
        self.center_x_position = center_x_position
        self.center_y_position = center_y_position
        self.radius = radius

    def is_point_in_the_circle(self, point):
        if (point.x_position - self.center_x_position)**2 + \
           (point.y_position - self.center_y_position)**2 <= self.radius:
            return True
        else:
            return False


point = Point(3, 4)
circle = Circle(3, 4, 5)
circle.is_point_in_the_circle(point)  # True
circle1 = Circle(-3, 4, 5)
circle1.is_point_in_the_circle(point)  # False

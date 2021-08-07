"""

*** EX 15.1 ***
    Write a definition for a class names Circle
    with attributes center and radius,
    where center is a Point object and radius is a number

    Instantiate a Circle object that represents a circle
    with center at (150, 100) and radius 75

    Write a function names rect_in_circle that takes a Circle and a Rectangle
    and returns True if the Rectangle lies entirely in or on the boundary of the circle.

    Write a function named rect_circle_overlap that takes a Circle and a Rectangle
    and returns True if any of the corners of the Rectangle fall inside the Circle
    Or as a more challenging version, return True if any part of the Rectangle falls inside the Circle

"""
import math
import copy


class Point:
    """Coordinate in 2 dimension space

    attributes: x, y
    """


class Rectangle:
    """Rectangle with all sides parallel to the x, y axis

    attributes: width, height, corner(bottom left)
    """


class Circle:
    """Circle

    attributes: center, radius
    """


def get_distance(p1, p2):
    distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y))
    return distance


def move_point(p, dx=0, dy=0):
    new_point = copy.deepcopy(p)
    new_point.x += dx
    new_point.y += dy
    return new_point


def point_in_circle(p, cir):
    distance = get_distance(p, cir.center)
    if distance <= cir.radius:
        return True
    else:
        return False


def get_four_points(rect):
    p1 = rect.corner
    p2 = move_point(rect.corner, dx=rect.width)
    p3 = move_point(rect.corner, dy=rect.height)
    p4 = move_point(rect.corner, dx=rect.width, dy=rect.height)
    four_points = (p1, p2, p3, p4)
    return four_points


def get_longest_d(rect, cir):
    points = get_four_points(rect)
    l = [get_distance(point, cir.center) for point in points]
    return max(l)


def get_shortest_d(rect, cir):
    a1 = abs(cir.center.x - rect.corner.x)
    a2 = abs(cir.center.x - (rect.corner.x + rect.width))
    a3 = abs(cir.center.y - rect.corner.y)
    a4 = abs(cir.center.y - (rect.corner.y + rect.height))
    l = [a1, a2, a3, a4]
    return min(l)


def rect_in_circle(rect, cir):
    points = get_four_points(rect)
    for point in points:
        if not point_in_circle(point, cir):
            return False
    return True


def rect_circle_overlap(rect, cir):
    if get_longest_d(rect, cir) < cir.radius:
        if not rect_in_circle:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    awesome_circle = Circle()
    awesome_circle.center = Point()
    awesome_circle.center.x = 150
    awesome_circle.center.y = 100
    awesome_circle.radius = 75


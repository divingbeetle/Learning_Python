"""

*** EX 15.2 ***
    Write a function called draw_rect() that takes a
    Turtle object and a Rectangle and uses the Turtle to draw the Rectangle

    Write a function called draw_circle that takes a Turtle and a Circle and
    draws the Circle

"""
import turtle
import turtle_shapes as ts


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


def draw_rect(t, rect):
    ts.polyline(t, 1, rect.width, 90)
    ts.polyline(t, 1, rect.height, 90)
    ts.polyline(t, 1, rect.width, 90)
    ts.polyline(t, 1, rect.height, 90)


def draw_circle(t, circle):
    ts.circle(t, circle.radius)


if __name__ == "__main__":
    bob = turtle.Turtle()

    box = Rectangle()
    box.corner = Point()
    box.corner.x = 0
    box.corner.y = 0
    box.width = 100
    box.height = 200

    awesome_circle = Circle()
    awesome_circle.center = Point()
    awesome_circle.center.x = 150
    awesome_circle.center.y = 100
    awesome_circle.radius = 75

    # draw_rect(bob, box)
    draw_circle(bob, awesome_circle)
    turtle.mainloop()
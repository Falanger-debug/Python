from points import Point


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Incorrect coordinates, you must pass such arguments: x1 < x2 and y1 < y2")

        if not isinstance(x1, (int, float)) or not isinstance(y1, (int, float)) \
                or not isinstance(x2, (int, float)) or not isinstance(y2, (int, float)):
            raise TypeError("x and y must be numbers")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def area(self):
        return abs((self.pt1.x - self.pt2.x) * (self.pt1.y - self.pt2.y))

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y),
                         min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other):
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y),
                         max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self):
        x1, y1, x2, y2 = self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        return Rectangle(x1, y1, x, y), Rectangle(x, y1, x2, y), Rectangle(x1, y, x, y2), Rectangle(x, y, x2, y2)

    @classmethod
    def from_points(cls, pts):
        if len(pts) != 2:
            raise ValueError("You must pass exactly 2 points")
        return cls(pts[0].x, pts[0].y, pts[1].x, pts[1].y)

    @property
    def top(self):
        return self.pt2.y

    @property
    def left(self):
        return self.pt1.x

    @property
    def bottom(self):
        return self.pt1.y

    @property
    def right(self):
        return self.pt2.x
    
    @property
    def width(self):
        return self.pt2.x - self.pt1.x

    @property
    def height(self):
        return self.pt2.y - self.pt1.y

    @property
    def top_left(self):
        return Point(self.pt1.x, self.pt2.y)

    @property
    def bottom_left(self):
        return Point(self.pt1.x, self.pt1.y)

    @property
    def top_right(self):
        return Point(self.pt2.x, self.pt2.y)

    @property
    def bottom_right(self):
        return Point(self.pt2.x, self.pt1.y)

    @property
    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
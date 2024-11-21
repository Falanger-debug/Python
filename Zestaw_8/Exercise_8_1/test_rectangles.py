import pytest
from points import Point
from rectangles import Rectangle


def test_init():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.pt1 == Point(1, 2)
    assert rect.pt2 == Point(3, 4)

    rect_float = Rectangle(1.5, 2.5, 3.5, 4.5)
    assert rect_float.pt1 == Point(1.5, 2.5)
    assert rect_float.pt2 == Point(3.5, 4.5)

    with pytest.raises(ValueError):
        Rectangle(3, 4, 1, 2)
        Rectangle(1, 4, 3, 2)
        Rectangle(1, 2, 3, 1)
        Rectangle(1, 2, 3, 2)

    with pytest.raises(TypeError):
        Rectangle("a", 2, 3, 4)
        Rectangle(1, "a", 3, 4)
        Rectangle(1, 2, "a", 4)
        Rectangle(1, 2, 3, "a")

def test_str():
    assert str(Rectangle(1, 2, 3, 4)) == "[(1, 2), (3, 4)]"
    assert str(Rectangle(1.5, 2.5, 3.5, 4.5)) == "[(1.5, 2.5), (3.5, 4.5)]"

def test_repr():
    assert repr(Rectangle(1, 2, 3, 4)) == "Rectangle(1, 2, 3, 4)"
    assert repr(Rectangle(1.5, 2.5, 3.5, 4.5)) == "Rectangle(1.5, 2.5, 3.5, 4.5)"

def test_eq():
    assert Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4)
    assert Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 5)

def test_ne():
    assert Rectangle(1, 2, 3, 4) != Rectangle(1, 3, 3, 4)
    assert Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 5)

def test_center():
    assert Rectangle(1, 2, 3, 4).center == Point(2, 3)
    assert Rectangle(1.5, 2.5, 3.5, 4.5).center == Point(2.5, 3.5)

def test_area():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.area() == 4
    rect_1 = Rectangle(1.5, 2.5, 3.5, 4.5)
    assert rect_1.area() == 4


def test_move():
    rect = Rectangle(1, 2, 3, 4).move(1, 1)
    assert rect == Rectangle(2, 3, 4, 5)
    rect_1 = Rectangle(1.5, 2.5, 3.5, 4.5).move(1, 1)
    assert rect_1 == Rectangle(2.5, 3.5, 4.5, 5.5)


def test_intersection():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(2, 3, 4, 5)
    assert rect1.intersection(rect2) == Rectangle(2, 3, 3, 4)


def test_cover():
    rect1 = Rectangle(1, 2, 3, 4)
    rect2 = Rectangle(2, 3, 4, 5)
    assert rect1.cover(rect2) == Rectangle(1, 2, 4, 5)

def test_make4():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.make4() == (Rectangle(1, 2, 2, 3), Rectangle(2, 2, 3, 3), Rectangle(1, 3, 2, 4), Rectangle(2, 3, 3, 4))


def test_virtual_attributes():
    rect = Rectangle(1, 2, 3, 4)
    assert rect.left == 1
    assert rect.bottom == 2
    assert rect.right == 3
    assert rect.top == 4
    assert rect.width == 2
    assert rect.height == 2

    assert rect.top_left == Point(1, 4)
    assert rect.bottom_left == Point(1, 2)
    assert rect.top_right == Point(3, 4)
    assert rect.bottom_right == Point(3, 2)


def test_from_points():
    point1 = Point(1, 2)
    point2 = Point(3, 4)
    rect = Rectangle.from_points((point1, point2))
    assert rect == Rectangle(1, 2, 3, 4)

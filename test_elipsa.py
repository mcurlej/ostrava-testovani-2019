import math
from elipsa import ellipse_area

def test_ellipse_surface():
    assert ellipse_area(1, 1) == math.pi
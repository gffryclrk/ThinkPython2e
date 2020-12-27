"""Unit tests for shape objects created for Chapter 15 Exercise 1"""
import math
import unittest
import sys
sys.path.append('ch15/')
from ex_15_9_1 import Point, Rectangle, Circle, rect_in_circle, rect_circle_overlap, LineSegment, Line

class TestGeometry(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(Point(0, 0), 100, 100)

    def test_point_distance(self):
        """Helper method behaves as expected"""
        pointa = Point(0,0)
        pointb = Point(3,4)
        self.assertTrue(pointa.distance(pointb) == 5)
    
    def test_rectangle_has_4_corners(self):
        """created rectangle has 4 points"""
        self.assertTrue(len(self.rectangle.vertices()) == 4)

    def test_rectangle_diagonals(self):
        """ Assert lengths of two diagonals in rectangle are equal """
        vl = self.rectangle.vertices()
        d1 = math.sqrt((vl[0].x - vl[2].x)**2 + (vl[0].y - vl[2].y)**2)
        d2 = math.sqrt((vl[1].x - vl[3].x)**2 + (vl[1].y - vl[3].y)**2)
        self.assertTrue(d1 == d2)

    def test_rect_in_circle(self):
        """ Test rect_in_circle returns correct result """
        r1 = Rectangle(Point(0,0), width = 5, height = 3)
        c1 = Circle(Point(0, 0), radius = 6)

        self.assertTrue(rect_in_circle(c1, r1))
        r1.bl = Point(3, 0) # TODO: Create a shift method that moves shapes
        self.assertFalse(rect_in_circle(c1, r1))
        
        

    def test_line_distance(self):
        """ Test Line object distance method """
        l = Line(Point(0,0), Point(1,1))
        xy = Point(0, 2.5)
        
        half_hypoteneuse = math.sqrt((2.5 ** 2) + (2.5 ** 2)) / 2
        self.assertTrue(
            math.isclose(
                l.distance(xy), half_hypoteneuse
                )
            )

        xy = Point(0, 2)
        d = 2 * math.sin( math.pi / 4 )
        self.assertTrue(
            math.isclose(
                l.distance(xy), d
                )
            )
                
        
    @unittest.SkipTest
    def test_rect_circle_overlap(self):
        """ Test some expected values for this overlap function"""
        c = Circle(Point(), 5)
        r = Rectangle(Point(0, 5), 1, 1)

        self.assertTrue(rect_circle_overlap(c, r))

        r.bl = Point(4,3)
        self.assertTrue(rect_circle_overlap(c, r))

        r.bl = Point(3.75, 3.75)
        self.assertFalse(rect_circle_overlap(c, r))


    def test_line_segment_dot_product(self):
        """ Test vector dot product implementaiton from https://www.geeksforgeeks.org/minimum-distance-from-a-point-to-the-line-segment-using-vectors/"""
        a = Point(0, 0)
        b = Point(2, 0)
        e = Point(4, 0)

        ab = LineSegment(a, b)
        be = LineSegment(b, e)
        ae = LineSegment(a, e)

        self.assertTrue(ab.dot_product(be) == 4)
        self.assertTrue(ab.dot_product(ae) == 8)

    def test_line_segment_shortest_distance(self):
        a = Point(0, 0)
        b = Point(2, 0)
        e = Point(4, 0)

        ab = LineSegment(a, b)
        be = LineSegment(b, e)
        ae = LineSegment(a, e)

        self.assertTrue(ab.shortest_distance(e) == 2)

        b = Point(2, 2)
        e = Point(2, 0)

        ab = LineSegment(a, b)
        be = LineSegment(b, e)
        ae = LineSegment(a, e)

        d = 2 * math.sin( math.pi / 4 )
        
        self.assertTrue(
            math.isclose(
                ab.shortest_distance(e), d
                )
            )

if __name__ == '__main__':
    unittest.main()

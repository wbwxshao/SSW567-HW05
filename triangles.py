"""Xueshi Wang SSW 567 HW01
   2019.01.27
"""
import unittest
def classify_triangle(a_side, b_side, c_side):
    """The function returns a string that specifies
    whether the triangle is scalene, isosceles, or equilateral,
    and whether it is a right triangle as well."""
    result = ''
    if (a_side + b_side <= c_side) or (a_side + c_side <= b_side) or (b_side + c_side <= a_side): #check if triangle is valid
        return False
    else:
        if a_side^2 + b_side^2 == c_side^2 or a_side^2 + c_side^2 == b_side^2 or b_side^2 + c_side^2 == a_side^2:
            #determine if the triangle is right first
            result = 'right'
        elif a_side == b_side and b_side == c_side and a_side == c_side:
            result = 'equilateral'
            #if it is right and euilateral, the result will be right/equilateral
        elif a_side != b_side and a_side != c_side and b_side != c_side:
            result = 'scalene'
        elif (a_side == b_side and a_side != c_side) or (a_side == c_side and a_side != b_side) or (b_side == c_side and b_side != a_side):
            result = 'isosceles'
        return result

class TestClassifyTriangle(unittest.TestCase):
    """Test triangle class"""
    def test_case(self):
        """test triangle function"""
        self.assertEqual(classify_triangle(3, 4, 5), 'right')
        self.assertEqual(classify_triangle(4, 5, 3), 'right')
        self.assertEqual(classify_triangle(1, 2, 100), False)  #invalid triangle
        self.assertEqual(classify_triangle(3, 3, 3), 'equilateral')
        self.assertEqual(classify_triangle(3, 3, 4), 'isosceles')
        self.assertEqual(classify_triangle(4, 7, 9), 'scalene')
    def test_case2(self):
        """Negative tests"""
        self.assertNotEqual(classify_triangle(3, 3, 3), 'right')
        self.assertNotEqual(classify_triangle(3, 3, 4), 'equilateral')
        self.assertNotEqual(classify_triangle(1, 2, 100), 'scalene')
        self.assertNotEqual(classify_triangle(10, 10, 10), 'isoceles')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

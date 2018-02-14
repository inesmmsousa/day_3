'''
Created on 07/02/2018

@author: Utilizador
'''
import unittest
from shapes import Shape, Rectangle

class Test(unittest.TestCase):


    def test_shape(self):
        shape = Shape((0,0,0), 'wood')
        self.assertEqual('Color: (0, 0, 0)    Material: wood    max_temperature: 20', str(shape))
        shape2 = Shape((0,0,0), 'wood') 
        self.assertEqual(shape, shape2)
        shape3 = Shape((0,23,0), 'woodds')
        self.assertEqual(shape, shape3)
        
    def test_rectangle(self):
        rectangle =  Rectangle(10, 20, (0,0,0), 'wood')
        self.assertEqual('Rectangle -> Comp. 10   Larg. 20    Color: (0, 0, 0)    Material: wood    max_temperature: 20', str(rectangle))
        self.assertEqual(200, rectangle.get_area())
        rectangle2 = Rectangle(10, 30 (0,0,0), 'wood')
        self.assertEqual(300, rectangle.get_area())
        self.assertNoEqual(rectangle2, rectangle)
        rectangle3 = Rectangle(10, 20, (0,0,0), 'wood')
        self.assertEqual(rectangle3, rectangle)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
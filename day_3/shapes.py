'''
Created on 07/02/2018

@author: Utilizador
'''
import math

from test.test_getargs2 import LARGE

class Shape(object):
    '''
    classdocs
    '''



    def __init__(self, color, material, max_temperature = 20):
        '''
        Constructor
        '''
        self.color = color
        self.material = material
        self.max_temperature = max_temperature
        
    def __str__(self):
        return 'color: {}  Material: {}    max_temperature {}'.format\
            (self.color, self.material, self.max_temperature)
    
    def __eq__(self, other):
        return self.color == other.color and\
            self.material == other.material and\
            self.max_temperature == other.max_temperature

class Rectangle(Shape):
    
    def __init__(self, comp, larg, color, material):
        Shape.__init__(self, color, material)
        self.comp = comp
        self.larg = larg

    def get_area(self):
        return self.comp * self.larg
    
    def __str__(self):
        return 'Rectangle -> Comp. {}   Larg. {}   {}'.format(\
            self.comp, self.larg, super(Rectangle, self).__str__())
    
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.comp == other.comp and self.larg == other.larg\
            and super(Rectangle, self).__eq__(other)   
            
            
class Circle(Shape):
    def __int__(self, raio, color, material):
        Shape.__init__(self, color, material)
        self.raio = raio 
        
    def get_area(self):
        return 2 * math.pi * (self.raio **2)
    
    def __str__(self):
        return 'Circle ->  raio. {}    {}'.format(self.raio, super(Circle, self).__str__())
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radious == other.radious\
            and super(Circle, self).__eq__(other) 

            
class Triangle(Shape):
    
    def __init__(self, cat1, cat2, color, material):
        Shape.__init__(self, color, material)
        self.cat1 = cat1
        self.cat2 = cat2

    def get_area(self):
        return (self.cat1 * self.cat2)/2
    
    def __str__(self):
        return 'Triangle -> Cat1. {}   Cat2. {}   {}'.format(\
            self.cat1, self.cat2, super(Triangle, self).__str__())
    
    def __eq__(self, other):
        return isinstance(other, Triangle) and self.cat2 == other.cat2 and self.cat1 == other.cat1\
             and super(Triangle, self).__eq__(other)   
   
class Shapes():
    
    def __init__(self):
        self.lst_shapes = []
        
    def add_shape(self, shape):
        if (shape not in self.lst_shapes):
            self.lst_shapes.append(shape)
            
    def print_areas(self):
        for shape_temp in self.lst_shapes:
            print(shape_temp)   
            print(shape_temp.get_area())
            
## start processing
if __name__ == '__main__':
    
    
    shapes = Shapes()
    shapes.add_shape(Rectangle(10,20,(0,0,0), 'wood'))
    shapes.add_shape(Rectangle(10,20,(0,0,0), 'wood'))
    shapes.add_shape(Triangle(10,20,(0,0,0), 'metal'))
    shapes.add_shape(Circle(10,(0,0,0), 'glass'))
    shapes.add_shape(Circle(10,(255,0,0), 'glass'))
    shapes.print_areas()
    
    rect1 = Rectangle(10, 20, (0,0,0), 'wood')
    print(rect1, rect1.get_area())
    
#     shape1 = shape((0,0,0), 'wood')
#     shape3 = shape((0,0,0), 'wood')
#     shape2 = shape((255,255,255), 'glass')
#     print(shape1)
#     print(shape2)
#     print(shape1 == shape2)
#     lst_shape = [shape1, shape2]
#     if (shape3 not in lst_shape):
#         lst_shape.append(shape3)
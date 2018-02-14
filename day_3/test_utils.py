'''
Created on 07/02/2018

@author: Utilizador
'''
import unittest
import utils

class Test(unittest.TestCase):


    def test_vect_float(self):
        self.assertIsNone(utils.vect_float('valor'))
        self.assertEqual(10, utils.vect_float('10'))
        self.assertEqual(10, utils.vect_float(10))
        self.assertIsNone(utils.is_number('valor'))
        self.assertEqual(10, utils.is_number('10'))
        self.assertEqual(10, utils.is_number(10))
    
    def runTest(self):   
        self.test_vect_float() 
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
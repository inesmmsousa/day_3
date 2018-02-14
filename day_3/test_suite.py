'''
Created on 07/02/2018

@author: Utilizador
'''

import unittest
import test_utils
import test_clean_fasta

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_utils.Test())
    suite.addTest(test_clean_fasta.Test())
    return suite
    
    
if __name__ == '__main__':
    
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)
'''
Created on 07/02/2018

@author: Utilizador
'''
import unittest
import second_module


class Test(unittest.TestCase):


    def test_clean_fasta(self):
        self.assertEqual('AAACCCTTT', second_module.clean_fasta('aaacccttt'))
        self.assertEqual('AAACCCTTT', second_module.clean_fasta('AAACCCTTT'))
        self.assertEqual('AAACCCTTT', second_module.clean_fasta('sdfdvaaacccttt'))
        self.assertEqual('', second_module.clean_fasta(''))
        self.assertEqual('AAACCCTTT', second_module.clean_fasta('aaacccttt'))

    def test_complement(self):
        self.assertEqual('AATT', second_module.complement('TTAA'))
        self.assertEqual('AATTGGCC', second_module.complement('TTAACCGG'))
        
    def test_reverse(self):
        self.assertEqual('TTAA', second_module.reverse('AATT'))
        
    def runTest(self):   
        self.test_clean_fasta()
        self.test_complement()
        self.test_reverse()  
        
        
                 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
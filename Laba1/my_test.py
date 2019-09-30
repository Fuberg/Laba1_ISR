'''
Test cases for PyEval

Jon Fincher, July 2018
'''
import unittest
from pyeval_expression import Expression
from proj.calc import *

class TestPyEval(unittest.TestCase):

    '''
    Validation of Expression and Operator classes.
    No setup function is needed
    '''

    def test_input(self):
        '''
        Tests a single positive operand expression
        '''
        outputData = dataHandler(25.0, 15.0, '+')
        self.assertEqual(str(outputData.handler()) , "Ответ : 40.0")

    
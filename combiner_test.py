from cgitb import reset
from linecache import getline
import unittest
import unittest
from csv_combiner import CSVCombiner
import pandas as pd

class testCases(unittest.TestCase):
    def test_checkFile1(self):
        file=""
        result = CSVCombiner().checkFile("")
        self.assertFalse(result)
        

    def test_checkFile2(self):
        file="./fixtures/empty.csv"
        result = CSVCombiner().checkFile(file)
        self.assertFalse(result)
        
    
    def test_checkFile3(self):
        file="./filedoesnotexist.csv"
        result = CSVCombiner().checkFile(file)
        self.assertFalse(result)

    def test_checkFile4(self):
        file="./fixtures/clothing.csv"
        result = CSVCombiner().checkFile(file)
        self.assertTrue(result)

    def test_checkFile5(self):
        file="./fixtures/hello.txt"
        result = CSVCombiner().checkFile(file)
        self.assertFalse(result)

    def test_readFile(self):
        file="./fixtures/clothing.csv"
        result = CSVCombiner().readFile(file)
        self.assertIsInstance(result, pd.DataFrame)

    def test_main(self):
        result = CSVCombiner().main(mode='unittest')
        self.assertEqual(len(result.split('\n')), 344)

if __name__ == '__main__':
    unittest.main()

'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
'''

import booksdatasource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = booksdatasource.BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))
     '''
     List of tests : 
     - one for creating instance variable 
     - 
     '''
    def test_instance_initiation(self):
      test_line = "The Fire Next Time,1963,James Baldwin (1924-1987)"
      self.assertTrue(BooksDataSource.__init__(test_line))

if __name__ == '__main__':
    unittest.main()
    

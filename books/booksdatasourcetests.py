'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021

   Partners : Nate and Shreya
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
        self.assertTrue(authors[0] == booksdatasource.Author('Pratchett', 'Terry'))

    # Checks that return type of .authors function is a list
    def test_authors_return(self):
        authors = []
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Smith"))

    def test_author_return_value(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        authors = [auth1]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Baldwin"))

    def test_author_order(self):
        auth1 = booksdatasource.Author("Brontë", "Ann", 1820, 1849)
        auth2 = booksdatasource.Author("Brontë", "Charlotte", 1816, 1855)
        authors = [auth2, auth1]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Brontë"))

    def test_book_return(self):
        books1 = []
        self.assertEqual(books1,booksdatasource.BooksDataSource.books("Blue"))

    def test_book_return_value(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        authors = [auth1]
        book1 = booksdatasource.Book("The Fire Next Time", 1963, authors )
        bookslist = [book1]
        self.assertEqual(bookslist, booksdatasource.BooksDataSource.books("The Fire Next Time", "title"))

    def test_book_order(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        auth2 = booksdatasource.Author("Orange", "Tommy", 1982)
        author_b = [auth1]
        author_o = [auth2]
        book1 = booksdatasource.Book("The Fire Next Time", 1963, author_b)
        book2 = booksdatasource.Book("There, There", 2018, author_o )
        bookslist = [book1, book2]
        temp = [booksdatasource.BooksDataSource.books("The", "title")]
        self.assertTrue(temp.__contains__(bookslist))


    def test_booksbwyrs_return(self):
        booklist =[]
        self.assertEqual(booklist, booksdatasource.BooksDataSource.books_between_years(2030, 2038))

    def test_booksbwyrs_return_value(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        author_b = [auth1]
        book1 = booksdatasource.Book("The Fire Next Time", 1963, author_b)
        bookListYrs = [book1]
        self.assertEqual(bookListYrs, booksdatasource.BooksDataSource.books_between_years(1963, 1963))

    def test_booksbwyrs_order(self):
        auth1 = booksdatasource.Author("Willis", "Connie", 1945)
        author_w = [auth1]
        auth2 = booksdatasource.Author("Murakami", "Haruki", 1949)
        author_m = [auth2]
        book1 = booksdatasource.Book("Blackout", 2010, author_w)
        book2 = booksdatasource.Book("1Q84", 2009, author_m)
        bookListyrs = [book2, book1]
        self.assertEqual(bookListyrs, booksdatasource.BooksDataSource.books_between_years(2009, 2010))





if __name__ == '__main__':
    unittest.main()
    

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

    # Checks that the return of an unspecified call to author returns all the
    def test_authors_return_full(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        auth2 = booksdatasource.Author("Brontë", "Charlotte", 1816, 1855)
        auth3 = booksdatasource.Author("Brontë", "Ann", 1820, 1849)
        authors = [auth1, auth3, auth2]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors(self))

    def test_author_return_value(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        authors = [auth1]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Baldwin"))

    def test_author_return_value_half(self):
        auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
        auth2 = booksdatasource.Author("Brontë", "Charlotte", 1816, 1855)
        authors = [auth1]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Bald"))

    def test_author_order(self):
        auth1 = booksdatasource.Author("Brontë", "Ann", 1820, 1849)
        auth2 = booksdatasource.Author("Brontë", "Charlotte", 1816, 1855)
        authors = [auth2, auth1]
        self.assertEqual(authors, booksdatasource.BooksDataSource.authors("Brontë"))

    def test_book_return(self):
        bookslist = []
        self.assertEqual(bookslist,booksdatasource.BooksDataSource.books("Blue"))

    # def test_book_return_full(self):
    #     auth1 = booksdatasource.Author("Baldwin", "James", 1924, 1987)
    #     auth2 = booksdatasource.Author("Brontë", "Charlotte", 1816, 1855)
    #     auth3 = booksdatasource.Author("Brontë", "Ann", 1820, 1849)
    #     auth4 = booksdatasource.Author("Orange", "Tommy", 1982)
    #     auth5 = booksdatasource.Author("Willis", "Connie", 1945)
    #     auth6 = booksdatasource.Author("Murakami", "Haruki", 1949)
    #     authors = [auth1, auth3, auth2]
    #     a1 = [auth1]
    #     a2 = [auth2]
    #     a3 = [auth3]
    #     a4 = [auth4]
    #     a5 = [auth5]
    #     a6 = [auth6]
    #     book1 = booksdatasource.Book("The Fire Next Time", 1963, authors)
    #     book2 = booksdatasource.Book("There, There", 2018, a)
    #
    #     bookslist = []
    #     self.assertEqual(bookslist,booksdatasource.BooksDataSource.books("Blue"))

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
        booklistyrs = [book1]
        self.assertEqual(booklistyrs, booksdatasource.BooksDataSource.books_between_years(1963, 1963))

    def test_booksbwyrs_order(self):
        auth1 = booksdatasource.Author("Willis", "Connie", 1945)
        author_w = [auth1]
        auth2 = booksdatasource.Author("Murakami", "Haruki", 1949)
        author_m = [auth2]
        book1 = booksdatasource.Book("Blackout", 2010, author_w)
        book2 = booksdatasource.Book("1Q84", 2009, author_m)
        booklistyrs = [book2, book1]
        self.assertEqual(booklistyrs, booksdatasource.BooksDataSource.books_between_years(2009, 2010))



# Test for when the list returns how many we need exact, when there is only a partial name, name that doesn't exist

if __name__ == '__main__':
    unittest.main()
    

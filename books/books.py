'''
    Authors : Nate and Shreya
    Revised By: Nate Przybyla
    For course CS 257 Books Project
    October 1st, 2021
'''
import sys

import booksdatasource


class Books:
    debug = False

    def help_txt(self):
        log = open("usage.txt", "r").read()
        print(log)
        sys.exit()

    def book_search(self, arguments):
        new_search_b = booksdatasource.BooksDataSource(sys.argv[1])
        if len(sys.argv) == 3:
            results = new_search_b.books(None, 'title')
            return results
        elif len(sys.argv) == 4:
            print("Wrong command line syntax, refer to usage statements by using -h or --help")
            return []  # call help
        elif len(sys.argv) == 5:
            if self.debug:
                print("here args are 6 so printing by title or year")
            if sys.argv[3].strip() == "-p":
                results = new_search_b.books(sys.argv[4], 'year')
                return results
            elif sys.argv[3].strip() == "-ti":
                results = new_search_b.books(sys.argv[4], 'title')
                return results
        else:
            return []

    def author_search(self, arguments):
        new_search_a = booksdatasource.BooksDataSource(sys.argv[1])
        if sys.argv[2] == "-a" or sys.argv[2] == "--author":
            if self.debug:
                print("in author search")
            if len(sys.argv) == 3:
                results = new_search_a.authors()
                return results
            elif len(sys.argv) == 4:
                results = new_search_a.authors(sys.argv[3])
                return results
            else:
                return []

    def year_search(self, arguments):
        if sys.argv[2] == '-y' or sys.argv == '--year':
            new_search_y = booksdatasource.BooksDataSource(sys.argv[1])
            if sys.argv[3].isnumeric():
                if len(sys.argv) == 4:
                    results = new_search_y.books_between_years(sys.argv[3], None)
                    return results
                elif sys.argv[4].isnumeric():
                    results = new_search_y.books_between_years(sys.argv[3], sys.argv[4])
                    return results
        else:
            return []

    def print_books(self, results):
        for book in results:
            if self.debug:
                print("new book print ", book)
            auth_line = ""
            for auth in book.authors:
                auth_line = auth_line + auth.given_name + " " + auth.surname + " " + auth.birth_year + "-" + \
                            str(auth.death_year) + " "
            print_line = book.title + ", " + book.publication_year + ", " + auth_line
            print(print_line)

    def print_auth(self, results):
        auth_line = ""

        for auth in results:
            auth_line = ""
            auth_line = auth_line + auth.given_name + " " + auth.surname + " " + str(auth.birth_year) + "-" + \
                        str(auth.death_year) + " "
            print(auth_line)


# Here the instantiation and main functionalities begin
def main():
    new_book_program = Books()
    if "--help" in sys.argv or "-h" in sys.argv:
        new_book_program.help_txt()
    else:
        # Sees which option the user wants to use
        if len(sys.argv) == 2:
            print("You require a search option, here are the usage statements, please run again")
            new_book_program.help_txt()

        elif sys.argv[2] == "-b" or sys.argv[2] == "--books":
            results = new_book_program.book_search(sys.argv)
            if len(results) == 0:
                print("Sorry, no items came up with your search, please try again.")
                sys.exit()
            else:
                new_book_program.print_books(results)
        elif sys.argv[2] == "-a" or sys.argv[2] == "--author":
            results = new_book_program.author_search(sys.argv)
            if len(results) == 0:
                print("Sorry, no items came up with your search, please try again.")
                sys.exit()
            else:
                new_book_program.print_auth(results)
        elif sys.argv[2] == "-y" or sys.argv[2] == "--year":
            results = new_book_program.year_search(sys.argv)
            if len(results) == 0:
                print("Sorry, no items came up with your search, please try again.")
                sys.exit()
            else:
                new_book_program.print_books(results)

        else:
            print("Invalid syntax. Refer to usage statements using -h or --help and rerun")

if __name__ == "__main__":
    main()

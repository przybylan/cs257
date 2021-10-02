'''
    Authors : Nate and Shreya
    For course CS 257 Books Project
    October 1st, 2021
'''
import sys

import booksdatasource


class Books:
    # python3 books.py --search/-s "filename" -[option]/--[option] OR python3 books.py -h/--help
    prndbg = False

    def help_txt(self):
        log = open("usage.txt", "r").read()
        print(log)
        sys.exit()

    def book_option(self, arguments):
        new_search_b = booksdatasource.BooksDataSource(sys.argv[2])
        # if arguments[3] == "-b" or arguments[3] == "--books":
        #     if self.prndbg:
        #         print("past book command check")
        if len(sys.argv) == 4:
            results = new_search_b.books(None, 'title')
            return results
        elif len(sys.argv) == 5:
            print("Wrong command line syntax, refer to usage statements by using -h or --help")
            return []  # call help
        elif len(sys.argv) == 6:
            if self.prndbg:
                print("here args are 6 so printing by title or year")
            if sys.argv[4].strip() == "-p":
                results = new_search_b.books(sys.argv[5], 'year')
                return results
            elif sys.argv[4].strip() == "-ti":
                # print(self.new_search.books(sys.argv[5], 'title'))
                results = new_search_b.books(sys.argv[5], 'title')
                return results
        else:
            return []

    def author_option(self, arguments):
        new_search_a = booksdatasource.BooksDataSource(sys.argv[2])
        if sys.argv[3] == "-a" or sys.argv[3] == "--author":
            if self.prndbg:
                print("in author search")
            if len(sys.argv) == 4:
                results = new_search_a.authors()
                return results
            elif len(sys.argv) == 5:
                results = new_search_a.authors(sys.argv[4])
                return results
            else:
                return []

    def year_option(self, arguments):
        return []
    def print_books(self, results):
        for book in results:
            if self.prndbg:
                print("new book print ", book)
            auth_line = ""
            #prev_auth =
            for auth in book.authors:
                #
                auth_line = auth_line + auth.given_name + " " + auth.surname + " " + auth.birth_year + "-" + \
                            str(auth.death_year) + " "
                #prev_auth = auth
            print_line = book.title + ", " + book.publication_year + ", " + auth_line
            print(print_line)

    def print_auth(self, results):
        auth_line = ""

        for auth in results:
            #if prev_auth == auth:
                #break
            auth_line = ""
            auth_line = auth_line + auth.given_name + " " + auth.surname + " " + str(auth.birth_year) + "-" + \
                        str(auth.death_year) + " "
            print(auth_line)
            #prev_auth = auth


# Here the instantiation and main functionalities begin
if "--search" in sys.argv or "-s" in sys.argv:
    new_book_program = Books()
    if "--help" in sys.argv or "-h" in sys.argv:
        new_book_program.help_txt()
    else:
        # if "." not in sys.argv[2]:
        #     print("Invalid syntax, please refer to usage statement")
        #     new_book_program.help_txt()
        # # else:
        #     new_search = booksdatasource.BooksDataSource(sys.argv[2])
        if len(sys.argv) == 3:
            print("You require a search option, here are the usage statements, please run again")
            new_book_program.help_txt()

        elif sys.argv[3] == "-b" or sys.argv[3] == "--books":
            results = new_book_program.book_option(sys.argv)
            if len(results) == 0:
                print("Sorry, no items came up with your search, please try again.")
                sys.exit()
            else:
                new_book_program.print_books(results)
        elif sys.argv[3] == "-a" or sys.argv[3] == "--author":
            results = new_book_program.author_option(sys.argv)
            if len(results) == 0:
                print("Sorry, no items came up with your search, please try again.")
                sys.exit()
            else:
                new_book_program.print_auth(results)
        #elif sys.argv[3] == "-y" or sys.argv[3] == "--year":
            #call the method, print handle empty/no results

else:
    print("Invalid syntax. Refer to usage statements using -h or --help and rerun")

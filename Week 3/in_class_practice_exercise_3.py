class Book:
    def __init__(self, title, author):
        self.title_of_book = title
        self.author_of_book = author

def display_books(books):
    for book in books:
        print(f"\"{book.title_of_book}\" by {book.author_of_book}")

def checkout_book(books):
    while(True):
        answer = input("\nPlease enter the title of the book you'd like to check out: ").lower()
        titles = []
        for book in books:
            titles.append(book.title_of_book.lower())
        if answer in titles:
            print(f"The book {answer.title()} is available and is now checked out to you!\n")
            for book in books:
                if (book.title_of_book.lower() == answer ):
                    books.remove(book)
                    break
            break
        else:
            print("The book you entered is not available.")

def main():
    book_1 = Book("The Lion, The Witch, and The Wardrobe", "C.S. Lewis")
    book_2 = Book("The Last Sin Eater", "Francine Rivers")
    book_3 = Book("Little Women", "Louisa May Alcott")
    books = [book_1, book_2, book_3]
    display_books(books)
    checkout_book(books)
    display_books(books)

main()
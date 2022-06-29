from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print(f'Oups, wrong option "{user_input}" selected')

        user_input = input(USER_CHOICE)


def prompt_add_book():
    print('\n *** Add a book :')
    book_name = input('Input a book title : ')
    book_author = input('Input book\'s author : ')

    # Envoie des infos pour ecriture
    database.add_book(book_name, book_author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f'{book["name"]} by {book["author"]}, read = {read}')


def prompt_read_book():
    print('\n *** Book read :')
    book_name = input('Input a book title : ')

    database.mark_book_as_read(book_name)


def prompt_delete_book():
    print('\n *** Delete a book from database :')
    book_delete = input('Input a book title : ')

    database.delete_book(book_delete)


menu()

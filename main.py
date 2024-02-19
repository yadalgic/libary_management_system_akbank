class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    # 2.a
    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("There is no books in library!")
            return
        print("*** List of Books ***")
        for book in books:
            title, author, release_date, num_of_pages = book.strip().split(',')
            print(f"Title: {title}, Author: {author}")

    # 2.b
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    #2.c
    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title_to_remove not in book:
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print(f"Book '{title_to_remove}' not found.")
            return
        self.file.seek(0)
        self.file.truncate(0)
        self.file.writelines(updated_books)
        print(f"Book '{title_to_remove}' removed successfully.")

lib = Library() #3.

#4.a
while True:
    print("\n*** MENU ***")
    print("1) List Books") #4.a.1
    print("2) Add Book") #4.a.2
    print("3) Remove Book") #4.a.3
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

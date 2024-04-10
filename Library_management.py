catalog={
    "1": {"title": "Book1", "author": "Author1", "quantity": 5},
    "2": {"title": "Book2", "author": "Author2", "quantity": 3},
    "3": {"title": "Book3", "author": "Author3", "quantity": 0},
}
userdata = {}
transactions=[]
def DisplayCatalog():
    print("Catalog:")
    for book_id, book in catalog.items():
        print(f"ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}")
def RegisterUser(user_id, name):
    userdata[user_id] = {"name": name, "books_checked_out": []}
def CheckoutBook(user_id, book_id, checkout_date):
    if book_id not in catalog:
        print("Book not found.")
        return
    if catalog[book_id]["quantity"] == 0:
        print("Book not available.")
        return
    if len(userdata[user_id]["books_checked_out"]) >= 3:
        print("User has reached the maximum limit of checked out books.")
        return
    catalog[book_id]["quantity"] -= 1
    userdata[user_id]["books_checked_out"].append({"book_id": book_id, "checkout_date": checkout_date})
    transactions.append({"user_id": user_id, "book_id": book_id, "transaction_type": "checkout"})
def ReturnBook(user_id, book_id, return_date):
    for book in userdata[user_id]["books_checked_out"]:
        if book["book_id"] == book_id:
            checkout_date = book["checkout_date"]
            days_checked_out = return_date - checkout_date
            if days_checked_out > 14:
                fine = days_checked_out - 14
                print(f"Book returned {days_checked_out - 14} days late. Fine: ${fine}")
            else:
                fine = 0
                print("Book returned on time.")
            catalog[book_id]["quantity"] += 1
            userdata[user_id]["books_checked_out"].remove(book)
            transactions.append({"user_id": user_id, "book_id": book_id, "transaction_type": "return", "fine": fine})
            return
    print("Book not found in user's checked out books.")
def ListOverdueBooks(user_id, return_date):
    overdue_books = []
    total_fine = 0
    for book in userdata[user_id]["books_checked_out"]:
        checkout_date = book["checkout_date"]
        days_checked_out = return_date - checkout_date
        if days_checked_out > 14:
            fine = days_checked_out - 14
            total_fine += fine
            overdue_books.append({"book_id": book["book_id"], "days_overdue": days_checked_out, "fine": fine})
    if overdue_books:
        print("Overdue Books:")
        for overdue_book in overdue_books:
            print(f"Book ID: {overdue_book['book_id']}, Days overdue: {overdue_book['days_overdue']}, Fine: ${overdue_book['fine']}")
        print(f"Total Fine: ${total_fine}")
    else:
        print("No overdue books.")
def ExtendDueDate(user_id, book_id):
    for book in userdata[user_id]["books_checked_out"]:
        if book["book_id"] == book_id:
            if "extension" in book:
                print("You have already extended the due date for this book.")
                return
            book["checkout_date"] += 7
            book["extension"] = True
            print("Due date extended by 7 days.")
            return
    print("Book not found in user's checked out books.")
def AddBook(book_id, title, author, quantity):
    catalog[book_id] = {"title": title, "author": author, "quantity": quantity}
def RemoveBook(book_id):
    if book_id in catalog:
        del catalog[book_id]
        print("Book removed from catalog.")
    else:
        print("Book not found in catalog.")
def DisplayMenu():
    print("\nMenu:")
    print("1. Display Catalog")
    print("2. Register User")
    print("3. Checkout Book")
    print("4. Return Book")
    print("5. List Overdue Books")
    print("6. Extend Due Date")
    print("7. Add Book to Catalog")
    print("8. Remove Book from Catalog")
    print("9. Exit")
def main():
    while True:
        DisplayMenu()
        choice = input("Enter your choice: ")
        if choice == "1":
            DisplayCatalog()
        elif choice == "2":
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            RegisterUser(user_id, name)
        elif choice == "3":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID to checkout: ")
            checkout_date = int(input("Enter checkout date (in days from today): "))
            CheckoutBook(user_id, book_id, checkout_date)
        elif choice == "4":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID to return: ")
            return_date = int(input("Enter return date (in days from checkout date): "))
            ReturnBook(user_id, book_id, return_date)
        elif choice == "5":
            user_id = input("Enter user ID: ")
            return_date = int(input("Enter return date (in days from today): "))
            ListOverdueBooks(user_id, return_date)
        elif choice == "6":
            user_id = input("Enter user ID: ")
            book_id = input("Enter book ID to extend due date: ")
            ExtendDueDate(user_id, book_id)
        elif choice == "7":
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter quantity: "))
            AddBook(book_id, title, author, quantity)
        elif choice == "8":
            book_id = input("Enter book ID to remove: ")
            RemoveBook(book_id)
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")
main()
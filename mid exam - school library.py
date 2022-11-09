books = input().split("&")
while True:
    commands = input()
    if commands == "Done":
        break
    commands = commands.split(" | ")
    if commands[0] == "Swap Books":
        command, first_book, second_book = commands[0], commands[1], commands[2]

        if first_book and second_book in books:
            first_book_index = books.index(first_book)
            second_book_index = books.index(second_book)
            books[first_book_index], books[second_book_index] = books[second_book_index],  books[first_book_index]


    else:
        command, book_name = commands[0], commands[1]
        if command == "Add Book":
            if book_name in books:
                continue
            else:

                books.insert(0, book_name)

        elif command == "Take Book":
            if book_name in books:
                books.remove(book_name)

        elif command == "Insert Book":
            if book_name in books:
                continue
            else:

                books.append(book_name)
        elif command == "Check Book":
            book_name = int(book_name)
            if book_name in range(len(books)):

                print(books[book_name])
            else:
                continue

print(", ".join(books))

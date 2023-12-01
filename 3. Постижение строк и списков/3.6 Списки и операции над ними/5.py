book_title = input()
author = input()
number_of_pages = int(input())
price = float(input())

book = [book_title, author, number_of_pages, price]
book[1] = "Пушкин"
del book[2]
book[2] = book[2] * 2

print(book)

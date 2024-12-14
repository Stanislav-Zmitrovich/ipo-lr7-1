books  = [
{"title": "Green mile", "author": "king", "year": 1996 },
{"title": "Harry potter", "author": "Rowling", "year": 1998},
{"title":"Metro", "author": "Glukhovsky", "year": 2002 },
{"title":"War and peace", "author": "Tolstoy", "year": 1998},
]
print (books) 
for book in books:

 print(f"Title: {book['title']}")
 print("--------")
 print(f"author: {book['author']}")
 print("--------")
 print(f"year: {book['year']}")
 print("--------")
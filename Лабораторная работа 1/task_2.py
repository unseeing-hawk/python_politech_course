# TODO Найдите количество книг, которое можно разместить на дискете

VOLUME_MB = 1.44
PAGES = 100
LINES = 50
SYMBOLS = 25
SYMBOL_B = 4

one_book_MB = SYMBOL_B * SYMBOLS * LINES * PAGES / 1024 / 1024

print("Количество книг, помещающихся на дискету:", int(VOLUME_MB // one_book_MB))

# Задание:
# Написать функцию, которая принимает на вход верхнеуровневый URL (строку), 
# а на выходе у нее — ZIP-архив со всеми PDF-файлами и извлеченным из них текстом 
# (просто в `.txt`), которые можно получить по этому URL и его дочерним адресам 
# (т.е. функция должна уметь ходить по ссылкам) 
# (упаковать через модуль `zipfile` стандартной библиотеки)

from pypdf import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
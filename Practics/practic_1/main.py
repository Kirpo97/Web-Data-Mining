# Практика 1. Упоминания кафедры ИТАС на сайтах города Перми
from comcrawl import IndexClient
import pandas as pd
import matplotlib.pyplot as plt

webresurs = [
    'https://pstu.ru/*',
    'http://itas.pstu.ru/*'
]

word = 'ИТАС'

# При поиске отбираем все с индексом "2019-47" (не совсем понятно что это за индекс. 
# Сначала я запустил метод без параметра и получил множество интексов, далее выбрал тот, который вернул код 200) (! На сайте CommonCrawl найдена база индексов)
# Судя по всему 2019 - это год индексации, -xx = ? (просто порядковый номер?)
client = IndexClient(indexes=['2019-47'])

count_itas = count_pstu = 0
path = './Practics/practic_1/file.csv'

for site in webresurs:
    client.search(site)
    # Исползуем все доступные потоки поцессора, в моём случае их 4
    client.download(threads=4)
    words = str(client.results).split()
    for i in words:
        if i == word:
            if site == webresurs[0]:  
                count_pstu += 1
                path = './Practics/practic_1/pstu.csv'
            else:
                count_itas += 1
                path = './Practics/practic_1/itas.csv'
                
            pd.DataFrame(client.results).to_csv(path)     
                       
print('\nhttps://pstu.ru/ = ', count_pstu)
print('\nhttp://itas.pstu.ru/ = ', count_itas)                 

plt.barh(range(2), [count_pstu, count_itas], align='center')
plt.yticks(range(2), webresurs, rotation='vertical')
plt.ylabel('Сайт')
plt.xlabel('Количество упоминаний')
plt.title('Упоминания слова ИТАС')
plt.show()

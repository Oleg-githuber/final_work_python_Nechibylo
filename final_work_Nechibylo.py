# import pandas as pd
from pandas import DataFrame, get_dummies    # Имрорт DataFrame
import random       # Импорт random для рандомного заполнения DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})       # Заполнение DataFrame рандомными значениями поля 'whoAmI'
#print(data.head(20))
print(data)     # Выводим DataFrame полностью, для чистоты эксперимента
print()
print("Результат работы программы:")
print()
new_data = get_dummies(data['whoAmI'])
print(new_data)
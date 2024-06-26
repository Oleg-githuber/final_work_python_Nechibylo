from pandas import DataFrame, get_dummies  # Имрорт DataFrame
import random  # Импорт random для рандомного заполнения DataFrame

lst = ['robot'] * 10    # Список из десяти строк 'robot'
lst += ['human'] * 10   # Добавляем к нему десять строк 'human'
random.shuffle(lst)     # Перемешиваем список
data = DataFrame({'whoAmI': lst})  # Заполнение DataFrame рандомными значениями поля 'whoAmI'
print(data.head(20))        # Выводим все 20 строк
print()
print("Результат работы программы:")
print()
# new_data = get_dummies(data['whoAmI'])
# print(new_data)
# Избавляемся от get_dummies
new_data = data     # Добавил DataFrame, чтобы изначальный оставить без изменений
data.loc[new_data['whoAmI'] == 'human', 'human'] = 'True'
data.loc[new_data['whoAmI'] != 'human', 'human'] = 'False'
data.loc[new_data['whoAmI'] == 'robot', 'robot'] = 'True'
data.loc[new_data['whoAmI'] != 'robot', 'robot'] = 'False'
print(new_data[['human', 'robot']].head(20))

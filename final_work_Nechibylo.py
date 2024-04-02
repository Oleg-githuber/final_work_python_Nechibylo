from pandas import DataFrame, get_dummies  # Имрорт DataFrame
import random  # Импорт random для рандомного заполнения DataFrame

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = DataFrame({'whoAmI': lst})  # Заполнение DataFrame рандомными значениями поля 'whoAmI'
print(data.head(20))        # Выводим все 20 строк
print()
print("Результат работы программы:")
print()
# new_data = get_dummies(data['whoAmI'])
# print(new_data)
# Избавляемся от get_dummies
data.loc[data['whoAmI'] == 'human', 'human'] = 'True'
data.loc[data['whoAmI'] != 'human', 'human'] = 'False'
data.loc[data['whoAmI'] == 'robot', 'robot'] = 'True'
data.loc[data['whoAmI'] != 'robot', 'robot'] = 'False'
print(data[['human', 'robot']].head(20))

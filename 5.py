# lst = [1,2,3,4,5]
# print(lst[-1])

# lst = [1,2,3,4,5]
# a,b,c, *d = lst
# print(d)

#можно изменять
# lst = [1,2,3]
# lst[0] = 'pisya'
# print(lst)

#можно добавлять
# lst = [1,2,3]
# lst.append('pisya')
# print(lst)

#вставка по индексу (все смещ вправо)
# lst = [1,2,3]
# lst.insert(0, 'pisya')
# print(lst)

#удаление по значению
# lst = [1,2,3]
# lst.remove(1)
# print(lst)

#удаление по индексу
# lst = [1,2,3]
# lst.pop(2)
# print(lst)

#удаление по диапозону индексов или по индексу
# lst = [1,2,3,4,5]
# del lst[0] # 2 3 4 5
# del lst[1:3] # удалит первый и второй 
# print(lst)

#чистка списка 
# lst = [1,2]
# lst.clear()
# print(lst)

#копирование .copy

# #обьединение
# lst = [1,2]
# lst2 = [3,4]
# print(lst+lst2)
# lst.extend(lst2)
# print(lst)

#подсчет .count

#поиск индекса элемента 
# lst = [1,2]
# print(lst.index(1))

#reverse() переворачивание списка

# #сортировка
# lst = [1,3,5,2,4]
# lst.sort() #или lst.sort(reverse=True)
# print(lst) 
# #можно также не изменяя исходный
# lstsorted = sorted(lst)
# print(lstsorted)


#_______________________tasks
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
# lst = []
# lst = [1,2,3,4,5]
# print(len(lst))
# print(lst[0], lst[2], lst[-1])
# mix_data = ['Michael', '21', 180]
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple']
# print(it_companies)
# print(len(it_companies))
# it_companies[0] = 'Keys'
# print(it_companies)
# it_companies.append('Ekra')
# print(it_companies)
# it_companies.insert(2, 'f5')
# print(it_companies)

#_____13
# it_companies[0] = it_companies[0].upper()
# print(it_companies)

#_____14
# str1 = '#'
# it_companies.extend(str1)
# print(it_companies)

#_____15
# x = 'Facebook' in it_companies
# print(x)

#_____16
# it_companies.sort()
# print(it_companies)

#_____17
# it_companies.reverse()
# print(it_companies)

#_____18
# it_companies2 = it_companies[3:]
# print(it_companies2)
# it_companies2 = it_companies[:3]
# print(it_companies2)

#_____20
# it_companies2 = it_companies[0:2]
# it_companies3 = it_companies[3:]
# print(it_companies2)
# print(it_companies3)
# print(it_companies2+it_companies3)

# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM']
#_____21
# it_companies.pop(1)
# print(it_companies)

#_______________________tasks
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages)
# print(ages[0])
# print(ages[-1])

# avg = sum(ages) / len(ages)
# print(avg)

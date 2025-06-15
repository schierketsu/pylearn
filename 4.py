# text1 = '''Я
# Саламон Михаил 
# Иванович '''
# print(text1)
# text2 = """Я
# Саламон Михаил 
# Иванович"""
# print(text2)

#________старый стиль
#%s - строка
#%d - целые
#%f - плав
# w1 = 'Sa'
# w2 = 'la'
# w3 = 'mon'
# w = '%s%s%s' %(w1,w2,w3)
# print(w)
# libr = ['A', 'B', 'C']
# z = 'вот и %s' % (libr)
# print(z) #вот и ['A', 'B', 'C']

#________новый стиль

# w1 = 'Sa' 
# w2 = 'la'
# w3 = 'mon'
# w = 'Моя фамилия {}{}{}' .format(w1,w2,w3)
# print (w)

# a=2
# b=3
# print('{}+{}'.format(a,b))
# print('{}+{}={}'.format(a,b,a+b))

#________интерполяция строк / f-строки
# a = 2
# b = 3
# print(f'{a}+{b}')
# print(f'{a}+{b}={a+b}')

#_________________________последовательности символов_________________________________________
#________распаковка
# word = 'salamon'
# a,b,c,d,e,f,g = word
# print(a) #s
#________по индексу
# word = 'salamon'
# let1 = word[0]
# print(let1) #s
# letlast = word[-1]  #-2 уже o
# print(letlast)
#________нарезка
# word = 'salamon'
# first3 = word[0:3] #первые 3
# print(first3)
# last4 = word[3:7] #последние 4
# print(last4)
# #или
# last4a = word[3:] #последние 4
# print(last4a)
#________переворот строки
# word = 'salamon'
# print(word[::-1])
#________пропуск символов при нарезке
# word = 'salamon'
# print(word[0:7:3])   #[start, stop, step], где start - начальный индекс, stop - конченый
#_________________________________________методы строк_________________________________________
# #capitalize()
# word = 'kakish'
# print(word.capitalize()) #Kakish

# #count()   count(substring, start=.., end=..)
# word = 'kakish'
# print(word.count('k'))
# print(word.count('k', 0, 2))

# #endswith()  проверяет, заканчивается ли строка указанным окончанием
# word = 'kakish'
# print(word.endswith('ish'))

# #find индекс первого вхождения
# word = 'kakish'
# print(word.find('kak'))

# #rfind индекс последнего вхождения
# word = 'kakish'
# print(word.rfind('k'))

#индексы вызывают исключение
#index()-первое rindex()-последнее
# word = 'kakish'
# subword = 'k'
# print(word.index(subword))

#join()
# words = ['a', 'b', 'c']
# res = ' '.join(words)
# print(res)
#_______________________tasks
# a = 'тридцать'
# b = 'дней'
# c = 'питона'
# print(f'{a} {b} {c}')

# let = 'Coding for all'
# print(let)
# print(len(let))
# print(let.upper())
# print(let.lower())

#___8
# let1 = 'coding'
# let2 = 'for'
# let3 = 'you'
# print(let1.capitalize() + " " + let2.capitalize() + " " + let3.capitalize() )
 
# word = 'coding for you'
# print(word.title())

# word = 'cODING fOR yOU'
# print(word.swapcase())

#___9
# word = 'Coding For All'
# print(word[7:])

#___10
# word = 'Coding For All'
# print(word.index('Coding'))

#___11
# word = 'Coding For All'
# print(word.replace('Coding', 'Python'))

#___13
# word = 'coding for you'
# print(word.split())

#___14
# words = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
# print(words.split(', '))

#___20
# text = 'coding for all'
# print(text.index('c'))

#___22
# text = 'coding for all'
# print(text.rfind('f'))

#___25
# text = 'tun tun tun tun tun - sahur'
# print(text[-5:])

#___28
# word = 'coding for all'
# sub = 'coding'
# if word.index(sub) == 0:
#     print('yes')
# else:
#     print('no')
#_______
# def f(word, sub):
#         if word.index(sub) == 0:
#             return 'yes'
#         return 'no'
# print(f('coding for all', 'for'))

#___29
# word = 'coding for all'
# print(word.endswith('all')) 

#___30
# word = '    coding for all    '
# print(word.strip(' '))

#___31
# a = '30DaysOfPython'
# b = 'thirty_days_of_python'
# print(a.isidentifier())
# print(b.isidentifier())

#___32
# words = ['D', 'F', 'B']
# res = ' # '.join(words)
# print(res)

#___33
# text = 'I am enjoying this challenge.\nI just wonder what is next'
# print(text)

#___34
# print('Name \t\tAge \tCountry \tCity\nAsabeneh \t250 \tFinland \tHelsinki')
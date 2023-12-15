# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# dict_tel = {"Ваня" : {"work" : 2345 , "home" : 123}, 
#             "Даня" : {"work" : 255 , "home" : 854}, 
#             "Петя" : {"work" : 864 , "home" : 658} }

import json

NameContact = None

phonebook = {NameContact : {'phones': [8311654654, 89654514], 
                            'birthday': "05.05.1990",'email' : "12@ya.ru"},
             "Дядя Вася" : {'phones': [54654541]}
            }
# print(phonebook['Дядя Ваня'])
# print(phonebook['Дядя Ваня'] ['phones'])
# print(phonebook['Дядя Ваня'] ['phones'][0])
# for name, values in phonebook.items():
#     print(name, values)

def help():
    selector = None
    try:
        selector = int(input('Введите "1" если хотите добавить контакт\n' + \
                             'Введите "2" если хотите сохранить новый контакт\n' + \
                             'Введите "3" если хотите загрузить контакт\n' + \
                             'Введите "4" если хотите найти контакт\n' + \
                             'Введите "5" если хотите удалить контакт\n' + \
                             'Введите номер соответствующий действию с контактом: '))
    except ValueError:
        print('\n\nНе корректный ввод!!!\n')
        print('Необходимо ввести целое число!!!\n\n')
    return selector

    

def load():
  
    try:
        with open("contacs.json", "r", encoding="utf-8") as fh:
             temp_contacts = json.loads(fh.read())
    except:
        print("Загрузили тестовый справочник")
        temp_contacts = {"Дядя Ваня" : {'phones': [8311654654, 89654514], 
                            'birthday': "05.05.1990",'email' : "12@ya.ru"},
             "Дядя Вася" : {'phones': [54654541]}
            }
    print("Загрузка прошла успешно")    
    return temp_contacts
    
phonebook = load()

# name = input("Введите имя пользователя: ")
# print(name)
# contact = {name: [8533122325, 8955221152],
#                'birthday': "01.04.1991", 'email': 'petrov@mail.ru'}

def save():
    with open("contacs.json", "w", encoding="utf-8") as fh:
              fh.write(json.dumps(phonebook, ensure_ascii=False))
    print("Ваш контакт успешно сохранен")


def find():
    try:
        with open("contacs.json", "r", encoding="utf-8") as fh:
             temp_contacts = json.loads(fh.read())
             if name in phonebook:
                 return print("Найден контакт: ", contact)
             
    except:
        return print("Контакта с таким именем нет")    
    
def delcontact():
     try:
          with open("contacs.json", "r", encoding="utf-8") as fh:
             temp_contacts = json.loads(fh.read())
          if name in phonebook:
               phonebook1 = phonebook.pop(name)
               return print("Контакт успешно удален", phonebook1)
          
     except:
          return print("Контакта с таким именем нет")

phonebook1 = phonebook
name = input("Введите имя Контакта: ")
contact = {name: [8533122325, 8955221152],
               'birthday': "01.04.1991", 'email': 'petrov@mail.ru'} 

while True:
    
     selector = help()
     if selector == 1:
         print("add")
         phonebook[name] = contact       
     elif  selector == 2:
         print(name)
         save()
     elif selector == 3:
         phonebook = load()
     elif selector == 4:
          find()
     elif selector == 5:
          delcontact()
          save()

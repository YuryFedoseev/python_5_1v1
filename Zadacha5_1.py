documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


    
def docum_people():
    #people
    inp_doc_people = input('Введите номер документа: ')
    n = 0
  
    for document in documents:
        if inp_doc_people == 'q':
            print('Выход выполнен')
            break 
        elif inp_doc_people == document.get("number"):
            name = document.get("name")
            print (f'Имя владельца документа: {name}')
            n += 1
    if n == 0:
        print ('Введены не верные данные')

            
def docum_shelf():
    #shelf
    inp_doc_people = input('Введите номер документа: ')
    n = 0
    for direct in directories.items():
        if inp_doc_people == 'q':
            print('Выход выполнен')
            break
        elif inp_doc_people in direct[1]:
             print (f'Документ лежит на полке: {direct[0]}')
             n += 1
    if n == 0:
         print('Введены не верные данные документа')


    
def docum_list():
    #list
    for document in documents:
        print (f'Список всех документов: {document.values()}')

        
def docum_add_test():
    #add
    print('Вы добавляете новый документ!')
    type_input = input('Введите тип документа (passport, invoice и т.д.): ')
    number_input = input('Введите номер документа: ')
    name_input = input('Введите имя человека: ')
    direct_input = input('Введите номер полки расположения документа: ')
    n=0
    for direct in directories.items():
        if (type_input == 'q' or number_input == 'q' or name_input == 'q' or direct_input == 'q'):
            print('Выход выполнен')
            break
        elif direct_input in direct[0]:
            set_doc = {"type":type_input,"number":number_input,"name":name_input}
            documents.append(set_doc)
            direct[1].append(number_input)
            print(f"Документы: {documents},'\n'")
            print(f"Полки: {directories}, '\n'")
            n += 1
    if n == 0:
        print ('Введены не верные данные полки')
    

def telo():
    print('p-(people)поиск человека по номеру документа','\n','s-(shelf)поиск документа на полке')
    print('l-(list)-все документы')
    print('a-(add)-добавление новых данных','\n','q-конец пути, покинь программу и иди домой')
    zadacha = input ('Введите нужную команду: ')
    zadacha = zadacha.lower()
    while True:
        if zadacha == 'p':
            docum_people()
        elif  zadacha == 's':
            docum_shelf()
        elif zadacha == 'l':
            docum_list()
        elif  zadacha == 'a':
            docum_add_test()
        elif  zadacha == 'q':
            break
        else:
            print('Введены не верные данные. Требуется ввести 1 букву на литиннице')
telo()

       

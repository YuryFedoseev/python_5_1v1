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
        print(' ')
    inp_doc_people = input('Запрос выполнен, Желаете повторить? Y - да, продолжить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'y':
        docum_people()
    elif inp_doc_people == 'n':
        telo()
        

            
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
    inp_doc_people = input('Запрос выполнен, Желаете повторить? Y - да, продолжить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'y':
        docum_shelf()
    elif inp_doc_people == 'n':
        telo()     


    
def docum_list():
    #list
    for document in documents:
        print (f'Список всех документов: {document.values()}')
        print (' ')
    inp_doc_people = input('Запрос выполнен, Желаете повторить? Y - да, продолжить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'y':
        docum_list()
    elif inp_doc_people == 'n':
        telo() 

        
def docum_add():
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
    inp_doc_people = input('Запрос выполнен, Желаете продолжить? Y - да, продолжить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'y':
        docum_add()
    elif inp_doc_people == 'n':
        telo()




def docum_dell():
    inp_doc_people = input('Введите номер удаляемого документа: ')
    n = 0
    import re
    for document in documents:
        if inp_doc_people == document.get("number"):
            n += 1
            #document = ''
            document.clear()
            # Не удаляет, остается пустой словарь
            print(documents)
            
            n = 0
            for direct in directories.items():
                if inp_doc_people == 'q':
                    print('Выход выполнен')
                    break
                elif inp_doc_people in direct[1]:
                    #print (f'Документ лежит на полке: {direct[0]}')
                    for dire in direct:
                        #print (f'dire: {dire}')
                        if inp_doc_people in dire:
                            perem_all = len(dire)
                            #perem_poz = re.search(inp_doc_people)
                            #perem_poz = dire.search(inp_doc_people)
                            perem_poz = re.dire(inp_doc_people)
                            print (f'dire: {perem_poz}')
                    n += 1
            
            if n == 0:
                print ('Данный документ отсутствует!')
    

#def docum_move():
    
def docum_as():
    inp_doc_people = input('Введите номер новой полки: ')
    dir_keys = set(directories.keys())
    n = 0
    for dir_key in dir_keys:
        if inp_doc_people == dir_key:
            print('Данная полка уже существует')
            n += 1
    if n < 1:
        directories[inp_doc_people]= []
        print (directories)        
    inp_doc_people = input('Запрос выполнен, Желаете повторить? Y - да, продолжить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'y':
        docum_as()
    elif inp_doc_people == 'n':
        telo() 
            

def telo():
    print(' p-(people)поиск человека по номеру документа','\n','s-(shelf)поиск документа на полке')
    print(' l-(list)-все документы')
    print(' a-(add)-добавление новых данных','\n','q-конец пути, покинь программу и иди домой')

    while True:
        zadacha = input ('Введите нужную команду: ')
        zadacha = zadacha.lower()
        if zadacha == 'q':
            break
        elif zadacha == 'p':
            docum_people()
        elif  zadacha == 's':
            docum_shelf()
        elif zadacha == 'l':
            docum_list()
        elif  zadacha == 'a':
            docum_add()  
        else:
            print('Введены не верные данные. Требуется ввести 1 букву на литиннице')
    inp_doc_people = input('Завершение работы... Желаете продолжить выход? Y - да, завершить работу; N - нет, вернуться в меню ')
    inp_doc_people = inp_doc_people.lower()
    if inp_doc_people == 'n':
        telo()
    elif inp_doc_people == 'y':
        raise SystemExit 

docum_dell()    


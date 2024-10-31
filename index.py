import json # импортируем модуль json для работы с файлами в формате JSON
# создаем функцию для вывода меню
def display_menu():
    print("Меню:") # выводим меню
    print("1. Вывести все записи") # выводим все записи
    print("2. Вывести запись по полю") # выводим запись по полю
    print("3. Добавить запись") # добавляем запись
    print("4. Удалить запись по полю") # удаляем запись по полю
    print("5. Выйти из программы") # выходим из программы
# загружаем записи из файла json
def load_data():
    try:
        with open('data1.json', 'r') as file: # пытаемся открыть файл на чтение
            data = json.load(file) # загружаем данные из файла в переменную data
    except FileNotFoundError: # если файл не найден
        data = [] # создаем пустой список данных
    return data # возвращаем загруженные данные
# сохраняем записи в файл json
def save_data(data):
    with open('data1.json', 'w') as file: # открываем файл на запись
        json.dump(data, file, indent=4) # сохраняем данные в файл с отступами для удобства чтения
# выводим все записи
def display_all_entries(data):
    for entry in data: # для каждой записи в данных
        print(entry) # выводим запись
# выводим запись по полю id
def display_entry_by_id(data, entry_id):
    for idx, entry in enumerate(data): # для каждой записи с её индексом
        if entry.get('id') == entry_id: # если id записи совпадает с искомым
            print(f"Запись с id {entry_id}: {entry}") # выводим запись
            print(f"Позиция в словаре: {idx}")  # выводим позицию записи в списке
            return # завершаем функцию
    print("Запись не найдена") # если запись не найдена, выводим сообщение
# добавляем новую запись
def add_entry(data):
    new_entry = {} # создаем новый словарь для записи
    new_entry['id'] = len(data) + 1 # присваиваем id новой записи
    new_entry['name'] = input("Введите имя: ") # запрашиваем имя у пользователя
    new_entry['age'] = input("Введите возраст: ") # запрашиваем возраст у пользователя
    data.append(new_entry) # добавляем новую запись в список данных
    save_data(data) # сохраняем изменённые данные в файле
    print("Запись добавлена успешно") # выводим сообщение о успешном добавлении записи
# удаляем запись по полю id
def delete_entry_by_id(data, entry_id): 
    for entry in data: # для каждой записи в данных
        if entry.get('id') == entry_id: # если id записи совпадает с искомым
            data.remove(entry)  # удаляем запись из списка данных
            save_data(data) # сохраняем изменённые данные в файле
            print(f"Запись с id {entry_id} удалена") # выводим сообщение об успешном удалении
            return # завершаем функцию
    print("Запись не найдена") # если запись не найдена, выводим сообщение
# основная часть программы
def main():
    data = load_data() # загружаем данные из файла
    while True: # бесконечный цикл для работы с меню
        display_menu() # выводим меню
        choice = input("Выберите пункт меню: ") # запрашиваем выбор у пользователя
        if choice == '1': # если пользователь выбрал пункт 1
            display_all_entries(data) # выводим все записи
        elif choice == '2': # если пользователь выбрал пункт 2
            entry_id = int(input("Введите id записи: ")) # запрашиваем id записи
            display_entry_by_id(data, entry_id) # выводим запись по id
        elif choice == '3': # если пользователь выбрал пункт 3
            add_entry(data) # добавляем новую запись
        elif choice == '4': # если пользователь выбрал пункт 4
            entry_id = int(input("Введите id записи для удаления: ")) # запрашиваем id записи для удаления
            delete_entry_by_id(data, entry_id) # удаляем запись по id
        elif choice == '5': # если пользователь выбрал пункт 5
            print(f"Количество операций с записями: {len(data)}") # выводим количество операций
            break # выходим из цикла
        else: # если пользователь ввел неверный пункт
            print("Неверный выбор. Попробуйте снова.") # выводим сообщение об ошибке
if __name__ == "__main__": # запускается ли текущий скрипт как основная программа или импортируется как модуль в другой скрипт 
    main() # запускаем основную функцию

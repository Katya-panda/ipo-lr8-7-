import json
# загружаем данные из файла (если файл существует)
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    data = []

# главное меню
while True:
    print("\nМеню:")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")
    choice = input("Выберите пункт меню (1-5): ")
    if choice == '1':
        # пункт “Вывести все записи”
        print("Все записи:")
        for idx, record in enumerate(data, 1):
            print(f"{idx}. {record}")
    elif choice == '2':
        # пункт “Вывести запись по полю”
        search_id = input("Введите ID записи для поиска: ")
        found = False
        for idx, record in enumerate(data, 1):
            if record.get('id') == search_id:
                print(f"Найдена запись: {record}, позиция в словаре: {idx}")
                found = True
                break
        if not found:
            print("Запись не найдена")
    elif choice == '3':
        # пункт “Добавить запись”
        new_record = {}
        new_record['id'] = input("Введите ID записи: ")
        new_record['data'] = input("Введите данные записи: ")
        data.append(new_record)
        print("Запись добавлена")
    elif choice == '4':
        # пункт “Удалить запись по полю”
        delete_id = input("Введите ID записи для удаления: ")
        for record in data:
            if record.get('id') == delete_id:
                data.remove(record)
                print("Запись удалена")
                break
        else:
            print("Запись не найдена")
    elif choice == '5':
        # пункт “Выйти из программы”
        print(f"Количество выполненных операций с записями: {len(data)}")
        with open('data.json', 'w') as file:
            json.dump(data, file)
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
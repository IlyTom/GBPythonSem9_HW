main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить файл',
             'Показать все контакты',
             'Добавить контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

select_menu = 'Выберите пункт меню: '

input_error = f'Ошибка ввода. Введите число от 1 до {len(main_menu) - 1}: '

new_contact = {'name': 'Введите имя контакта: ',
               'phone': 'Введите телефон: ',
               'comment': 'Введите комментарий: '}

empty_book = 'Телефонная книга пуста или не открыта'

load_successful = 'Телефонная книга успешно загружена'
save_successful = 'Телефонная книга успешно сохранена'
error_load = 'Ошибка загрузки телефонной книги'
error_save = 'Ошибка сохранения телефонной книги'


def add_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен в книгу!'


search_word = 'Введите строку для поиска: '
index_remove = 'Введите ID контакта, который хотите удалить: '

index_update = 'Введите ID контакта, который хотите изменить'


def empty_search(word: str) -> str:
    return f'Контакты содержащие {word} не найдены'


def remove_contact(name: str) -> str:
    return f'Контакт {name} успешно удален!'


def update_contact(name: str) -> str:
    return f'Контакт {name} успешно изменен'


change_confirm = 'У вас есть не сохраненые изменения. Сохранить перед выходом? (y/n)'

goodbay = 'До новых встреч, владыка!'

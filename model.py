import json

path = 'phones.json'
phone_book = {}


def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return phone_book
    except:
        return False


def save_file():
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False, indent=4)
        return True
    except:
        return False


def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1


def add_contact(new: dict[str, str]):
    contact = {check_id(): new}
    phone_book.update(contact)


def search(word: str) -> dict[int:dict[str, str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result


def update_contact(index, book: dict[str, str]):
    contact = {int(index): book}
    phone_book.update(contact)
    return phone_book[int(index)].get('name')



def remove(index):
    name = phone_book.pop(int(index))
    return name.get('name')

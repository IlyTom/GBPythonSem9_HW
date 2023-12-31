import text
import view
import model
def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if model.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if model.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(model.phone_book, text.empty_book)
            case 4:
                new = view.add_contact()
                model.add_contact(new)
            case 5:
                word = view.view_input(text.search_word)
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                word = view.view_input(text.search_word)
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                index = view.view_input(text.index_update)
                name = model.update_contact(index, view.update_contact())
                view.print_message(text.update_contact(name))
            case 7:
                word = view.view_input(text.search_word)
                result = model.search(word)
                view.show_contacts(result, text.empty_search(word))
                index = view.view_input(text.index_remove)
                name = model.remove(index)
                view.print_message(text.remove_contact(name))
            case 8:
                view.print_message(text.goodbay)
                break
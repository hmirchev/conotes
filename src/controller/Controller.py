import re
from src.ui.ConsoleUI import ConsoleUI
from src.model.Note import Note
from src.model.ToDo import ToDo
from src.plugins.PluginManager import PluginManager

class Controller(object):
    def __init__(self):
        self._ui = ConsoleUI()
        self._texts = list()

        plugin_manager = PluginManager()
        plugin_manager.collectPlugins()
        plugin_manager.loadPlugins()

    def process_main_menu(self):
        while True:
            choice = input(self._ui.main_menu())

            if choice == '0':
                break
            elif choice == '1':
                self.process_add_menu()
            elif choice == '2':
                self.process_edit_menu()
            elif choice == '3':
                self.process_remove_menu()
            elif choice == '4':
                self.process_find_menu()
            else:
                print("Illegal input. Should be in [0, 4]. Try again.")

    def process_add_menu(self):
        while True:
            choice = input(self._ui.add_menu())

            if choice == '0':
                break
            elif choice == '1':
                self._texts.append(self._get_note())
            elif choice == '2':
                self._texts.append(self._get_todo())
            else:
                print("Illegal input. Should be in [0, 2]. Try again.")
        self._print_all_texts()

    def _get_note(self):
        title = input("Enter title: ")
        description = input("Enter description: ")
        tags = input("Enter tags (comma-separated): ")
        tags = re.split(r'[,\s]\s*', tags)

        return Note(title, description, tags)

    def _get_todo(self):
        description = input("Enter description: ")
        begin_date = input("Enter begining date (e.g. 2001-12-25): ")
        end_date = input("Enter end date (e.g. 2001-12-25): ")
        tags = input("Enter tags (comma-separated): ")
        tags = re.split(r'[,\s]\s*', tags)

        return ToDo(description, begin_date, end_date, tags)

    def process_edit_menu(self):
        if not self._texts:
            print("There are no texts to edit. Try to add some texts.")
            return
        choice = int(input(self._print_all_texts()))
        all_texts = len(self._texts) - 1

        if 0 <= choice <= all_texts:
            if isinstance(self._texts[choice], Note):
                self._edit_note(choice)
            elif isinstance(self._texts[choice], ToDo):
                self._edit_todo(choice)
        else:
            print("Illegal input. Should be in [0, " +\
                  str(all_texts) + "] Try again.")
            return self.process_edit_menu()

    def _edit_note(self, index):
        while True:
            choice = input(self._ui.edit_note_menu())

            if choice == '0':
                break
            elif choice == '1':
                print("Current title: " + self._texts[index].title)
                new_title = input("Enter new title: ")
                self._texts[index].title = new_title
            elif choice == '2':
                print("Current description: " + self._texts[index].description)
                new_description = input("Enter new description: ")
                self._texts[index].description = new_description
            elif choice == '3':
                print("Current tags: " + str(self._texts[index].tags))
                tag = input("Enter new tag: ")
                self._texts[index].add_tag(tag)
            elif choice == '4':
                print("Current tags: " + str(self._texts[index].tags))
                tag = input("Enter tag to remove: ")
                self._texts[index].remove_tag(tag)
            else:
                print("Illegal input. Should be in [0, 4]. Try again.")

    def _edit_todo(self, index):
        while True:
            choice = input(self._ui.edit_todo_menu())

            if choice == '0':
                break
            elif choice == '1':
                print("Current description: " + self._texts[index].description)
                new_description = input("Enter new description: ")
                self._texts[index].description = new_description
            elif choice == '2':
                print("Current begining date: " + str(self._texts[index].begin_date))
                new_date = input("Enter new begining date (e.g. 2001-12-25): ")
                self._texts[index].begin_date = new_date
            elif choice == '3':
                print("Current end date: " + str(self._texts[index].end_date))
                new_date = input("Enter new end date (e.g. 2001-12-25): ")
                self._texts[index].end_date = new_date
            elif choice == '4':
                self._texts[index].finished = True
            elif choice == '5':
                self._texts[index].finished = False
            elif choice == '6':
                print("Current tags: " + str(self._texts[index].tags))
                tag = input("Enter new tag: ")
                self._texts[index].add_tag(tag)
            elif choice == '7':
                print("Current tags: " + str(self._texts[index].tags))
                tag = input("Enter tag to remove: ")
                self._texts[index].remove_tag(tag)
            else:
                print("Illegal input. Should be in [0, 7]. Try again.")

    def process_remove_menu(self):
        if not self._texts:
            print("There are no texts to remove. Try to add some texts.")
            return
        choice = int(input(self._print_all_texts()))
        all_texts = len(self._texts) - 1

        if 0 <= choice <= all_texts:
            self._texts.pop(choice)
        else:
            print("Illegal input. Should be in [0, " +\
                  str(all_texts) + "] Try again.")

    def process_find_menu(self):
        choice = input(self._ui.find_menu())

        if choice == '0':
            return

        pattern = input("pattern: ")
        for text in self._texts:
            found = text.matches(pattern)
            if choice == '2':
                found = found and isinstance(text, Note)
            elif choice == '3':
                found = found and isinstance(text, ToDo)

            if found:
                print(text)

    def _print_all_texts(self):
        return "\n".join("{}] {}".format(str(index), str(text))\
                        for index, text in enumerate(self._texts))

class ConsoleUI(object):
    def __init__(self): pass

    def main_menu(self):
        return "\n0.Exit\n1. Add...\n2. Edit..." +\
            "\n3. Remove...\n4. Find...\n"

    def add_menu(self):
        return "\n0.Back\n1. ...a note.\n2. ...a ToDo.\n"

    def edit_note_menu(self):
        return "\n0.Back\n1. Edit note's title.\n" +\
            "2. Edit note's description.\n3. Add tag.\n4. Remove tag.\n"

    def edit_todo_menu(self):
        return "\n0.Back\n1. Edit ToDo's description.\n" +\
            "2. Edit ToDo's begining date.\n3. Edit ToDo's end date." +\
            "\n4. Mark ToDo as finished.\n5. Mark ToDo as unfinished." +\
            "\n6. Add tag.\n7. Remove tag.\n"

    def find_menu(self):
        return "0.Back\n1. ...all that match...\n" +\
            "2. ...notes that match...\n3. ...ToDos that match...\n"

from core import Note, Notebook, JSONFile
from datetime import datetime

class ConsoleApp:
    def __init__(self):
        self.__notebook = Notebook(JSONFile('notes.json'))

    def show_notes(self):
        pass

    def __show_notes(self) -> None:
        all_notes = self.__notebook.get_notes()
        for note in all_notes:
            print(note)
    
    def __show_note(self) -> None:
        note_id = input("Enter note id: ")
        note = self.__notebook.get_note()
        print(note)

    def __add_note(self):
        note_id = input("Enter note id: ")
        text = input("Input text: ")

    def __update_note(self) -> None:
        note_id = input('Enter note id: ')
        note = self.__notebook()
        new_text = input("Enter new text: ")
        self.__notebook.update_note(
            Note(note_id, new_text,
                 datetime.now())
        )

    def _delete_note(self) -> None:
        note_id = input("Enter note id: ")

    def __show_menu(self):
        print("""
1. Show All Notes
2. Show note details
3. Write New Note
4. Update Note                                          """)
        
        
if __name__ == '__main__':
    app = ConsoleApp()
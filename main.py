from core import Note, Notebook, JSONFile


class Console:
    def __init__(self):
        self.__notebook = Notebook(JSONFile('notes.json'))

    def show_notes(self):
        pass
    

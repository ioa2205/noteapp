from note import Note
from storage import Storage
class Notebook:
    def __init__(self, storage: Storage) -> None:
        self.__storage = storage
        self.notes = self.__storage.load()
        
    def add_note(self, note: Note) -> None:
        """Add given Note object into existing list of notes"""
        pass

    def update_note(self, note: Note) -> None:
        pass

    def delete_note(self, note_id: int) -> None:
        pass

    def get_notes(self) -> list[Note]:
        return self.notes

    def get_note(self, note_id: int) -> Note:
        pass


if __name__ == '__main__':
    notebook1 = Notebook()
    notes = notebook1.notes
    print(notes)
from abc import ABC, abstractmethod
from note import Note
class Storage:
    
    @abstractmethod
    def save(self, notes: list[Note]) -> None:
        pass

    @abstractmethod
    def load(self) -> list[Note]:
        pass

    @property
    @abstractmethod
    def info(self) -> dict[str, str]:
        pass


class JSONFile(Storage):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def save(self, notes: list[Note]) -> None:
        print(f"{len(notes)} notes saved into file{self.file_name}")

    def load(self) -> list[Note]:
        return [Note(1, 'First Note', '2025-01-01'), Note(2, 'Second Note', '2025-01-01')]
    
    def info(self) -> dict[str, str]:
        return {'file_name': self.file_name}
    
class CSVFile(Storage):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    
    def save(self, notes: list[Note]) -> None:
        pass

    def load(self) -> list[Note]:
        pass

    def info(self) -> dict[str, str]:
        pass

    
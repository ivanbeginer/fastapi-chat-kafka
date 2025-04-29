from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TextToLongException(ApplicationException):
    text:str

    @property
    def message(self):
        return f'Слишком длинный текст сообщеня {self.text[:255]}'

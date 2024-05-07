from abc import ABC, abstractmethod


class FileSaver(ABC):
    """
    Абстрактный класс для работы с файлами
    """

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancy(self,*args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self,*args, **kwargs):
        pass
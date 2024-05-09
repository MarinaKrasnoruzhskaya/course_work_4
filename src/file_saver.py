import os
from abc import ABC, abstractmethod

from config import ROOT_DIR


class FileSaver(ABC):
    """
    Абстрактный класс для работы с файлами
    """
    def __init__(self, name):
        self.path_file = os.path.join(ROOT_DIR, "data", name)

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass

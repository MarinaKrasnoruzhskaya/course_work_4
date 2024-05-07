class EmptyList(Exception):
    """Класс-ошибка пустого списка"""
    def __init__(self, message=None):
        super().__init__(message)

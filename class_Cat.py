class Cat:
    def __init__(self, gender_arg: str, color_arg: str, age_arg: int):
        """
        Создание объекта 'Кошка'
        :param gender_arg: возраст кошки
        :param color_arg: цвет кошки
        :param age_arg: возраст кошки
        """
        self.gender_attr = gender_arg
        self.color_attr = color_arg
        self.age_attr = age_arg

    def is_cat(self) -> bool:
        """
        Функция для проверки, является ли объект Кошкой
        :return: является ли объект Кошкой, или нет?
        """
        ...

    def say_meow(self) -> str:
        """
        Функция для воспроизведения звука Кошкой, в разных ситуациях.
        Например, мурлыкание или мяуканье
        :return: текстовое описание воспроизведенного звука, например "Мяу" или "Муррр"
        """
        ...

    def catch_mouse(self, mouse: int) -> int:
        """
        Функция для подсчета пойманых мышей Кошкой
        :param mouse: колличество мышей в доме
        :return: колличество пойманных мышей
        """
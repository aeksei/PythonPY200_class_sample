class BoxOOP:
    def __init__(self, number_of_functions: int, number_of_variable: int):
        """
        Создание объекта Коробка ООП
        :param number_of_functions: количество "помещенных" в коробку функций
        :param number_of_variable: количество "помещенных" в коробку переменных
        """
        self.number_of_functions_attr = number_of_functions
        self.number_of_data_attr = number_of_variable

    def is_box_oop(self) -> bool:
        """
        Функция для проверки, является ли объект коробкой ООП
        :return: является или нет
        """
        ...

    def function(self, func: int) -> int:
        """
        Функция для подсчета количества функций внутри коробки ООП
        :param func: переданная, в коробку ООП, функция
        :return: количество переданных функции в коробку ООП
        """
        ...

    def variable(self, var: int) -> int:
        """
        Функция для подсчета количества переменных внутри коробки ООП
        :param var: переданная, в коробку ООП, переменная
        :return: количество переданных переменных в коробку ООП
        """
        ...


if  __name__ == "main":
    box_1 = BoxOOP(5, 10)
    box_2 = BoxOOP(4, 1)
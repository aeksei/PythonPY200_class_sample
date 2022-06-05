class Covid19:
    def __init__(self, date_of_virus_detection: str, country_of_virus_detection: str):
        """
        Создание объекта "Covid19"
        :param date_of_virus_detection: дата обнаружения вируса Covid19
        :param country_of_virus_detection: страна обнаружения вируса Covid19
        """
        self.date_of_virus_detection = date_of_virus_detection
        self.country_of_virus_detection_attr = country_of_virus_detection

    def is_covid19(self) -> bool:
        """
        Функция проверки, является ли объект "Covid19"
        :return: является или нет
        """
        ...

    def number_of_countries(self, countries: str) -> int:
        """
        Функция для подсчета стран, имеющих пациентов с Covid19
        :return: кол-во стран, имеющих пациентов с Covid19
        """
        ...

    def alphabetical_order_countries(self, countries: str) -> dict:
        """
        Функция для вывода названия стран в алфавитном порядке
        :param countries: название стран
        :return: вывод списка стран в алфавитном порядке
        """
        ...


if __name__ == "main":
    incident_1 = Covid19('25.03.2020', 'USA')
    incident_2 = Covid19('15.11.2021', 'Russia')
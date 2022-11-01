## Задание

1. Сделать fork данного репозитория.  
    Для этого в правом верхнем углу нажать на кнопку fork.

1. Придумать и написать 3 абстрактных класса, описывающих любой объект.  
   Каждый класс следует оформлять в отдельном модуле.  
   Например, в качестве объектов могут выступать материальные сущности стол, дерево, и даже нематериальные стек, Facebook.
    ```python
    class НазваниеКласса:
     ...
    ```
2. Для каждого класса выделить 2-3 характеристики и записать их в виде атрибутов.  
    Если на аргументы конструктора накладываются какие-то ограничения, которые в реальной жизни не допустимы,  
    то следует описать валидацию (проверку) этих аргументов. 
    ```python
    class НазваниеКласса:
        def __init__(self, arg1, arg2):
            # Атрибутам присваиваются значения аргументов конструктора объекта
            self.attr1 = arg1
            self.attr2 = arg2
    ```
3. Сформировать для каждого класса 2-3 метода, которые будет описывать возможные действия с объектом.  
   Реализацию самих методов писать не нужно, достаточно только названия.  
   Если на аргументы накладываются какие-то ограничения, которые в реальной жизни не допустимы,  
   то следует описать валидацию (проверку) этих аргументов. 
    ```python
    class НазваниеКласса:
        ...
    
        def method_1(self):
            # Реализацию методов не нужно, достаточно только заглушки в виде троеточия
            ...
    ```
   
4. Каждый метод должен содержать документацию с описанием аргументов(если они есть) и возвращаемого результата(если он есть).
5. Все аргументы методов и возвращаемые результаты должны содержать аннотацию типов.
6. В документации должен содержаться как минимум один [doctest](https://docs.python.org/3/library/doctest.html) пример как пользоваться методом. 
7. Результат представить в виде ссылки на репозиторий GitHub, 
   а ещё предпочтительнее в виде Pull Request без указания reviewer.

## Пример
[Пример](https://github.com/aeksei/PythonPY200_class_sample/blob/master/example.py) верно оформленного класса

# ООП - об'єктно орієнтоване програмування
# Клас - кастомний тип даних, який описує деякий об'єкт.
# Клас - креслення майбутнього екземпляра об'єкта.

# Інкапсуляція - приховування внутрішньої реалізації та надання санкціонованого доступу
# до інтерфейсу класу. Як чорна скринька.
# Абстрагуємося від внутрішньої реалізації.

# Спадкування - створення нового класу на основі вже існуючого.
# Розширення базового класу – дочірніми/дочірніми класами.
# Абстрагуємось від базового класу/класів, використовуючи дочірній клас.

# Поліморфізм - один інтерфейс та багато реалізацій.
# Абстрагуємося від конкретної реалізації

class Car:
    company_name = "Toyota"

    # конструктор без параметрів (не за замовчуванням)
    def __init__(self, color, engine):
        self.color = color
        self.engine = engine

    def show_info(self):
        print(f"Color: {self.color}, Engine: {self.engine}\n")

    @staticmethod # декоратор 
    def get_company_name():
        print(f"Company Name: {Car.company_name}")

    # конструктор класу - створює екземпляр об'єкту
    # def __new__(cls):
    #     pass

    # для ініціалізації об'єкту
    # якщо явно не визначити конструктор __new__ -> то __init__ він створиться автоматично
    # def __init__(self):
    #     pass


# toyota_1: Car = Car("green", "v8")
# print(toyota_1)
# # print(toyota_1.company_name)
# toyota_1.get_company_name()
# toyota_1.show_info()
#
# car_color = "red"
# car_engine = "v6"
# toyota_2: Car = Car(car_color, car_engine)
# print(toyota_2)
# # print(toyota_2.company_name)
# toyota_2.get_company_name()
# toyota_2.show_info()
#
# Car.show_info(toyota_1)
# Car.get_company_name()

###############
# статичний метод (функція), поле (змінна) відносяться до класу, і до екземпляра
# статичний ел-т можна використовувати не створюючи екземпляр класу
# Найчастіше статичні класи використовують для опису конфігів та інших службових об'єктів, там де немає сенсу
# створювати екземпляри

# __init__ Конструктор класу – дозволяє створити екземпляр класу. Можливо з параметрами та без параметрів.
# # self - посилання на контекст класу, екземпляр класу
# # контекст класу - все що є частиною класу (экземпляра)

# class InvoiceTypes:
#     URGENT = "Urgent invoice"
#     DELIVERED = "Delivered invoice"
#     PAYABLE = "Paid invoice"
#
#     @staticmethod
#     def get_invoice_types():
#         print(InvoiceTypes.URGENT)
#         print(InvoiceTypes.DELIVERED)
#         print(InvoiceTypes.DELIVERED)
#
#
# # print(InvoiceTypes.URGENT)
# InvoiceTypes.get_invoice_types()

#################################
# без инкапсуляции
class Person:
    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Hobby: {self.hobby}")


# vasya = Person("Vasya", 20, "work")
# vasya.show_info()
# vasya.name = ""  # некорректное значение
# vasya.show_info()
#
# petya = Person("", -20, "work")  # некорректные значения
# petya.show_info()

#################
# добавим инкапсуляцию
class User:
    __name = "no name"  # private поле, доступне тільки всередині цього класу
    __age = 18  # private поле, доступне тільки всередині цього класу

    def __init__(self, name, age, hobby="no hobby"):
        self.hobby = hobby

        # без использования инкапсуляции
        # self.__name = name  # private поле, доступне тільки всередині цього класу
        # self.__age = age  # private поле, доступне тільки всередині цього класу

        # применим инкапсуляцию V1
        # self.set_name(name)
        # self.set_age(age)

        # применим инкапсуляцию V2
        self.name = name  # под капотом мы обращаемся к @name.setter
        self.age = age   # под капотом мы обращаемся к @age.setter

    # предоставим санкционированный доступ к приватным полям через функции (V1)
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if 1 < len(name) < 30:
            self.__name = name
        else:
            print("Incorrect name length!")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 18 <= age < 150:
            self.__age = age
        else:
            print("Incorrect age!")

    # или предоставим санкционированный доступ к приватным полям через аннотации свойств (V2)
    # этот вариант предпочтительный для реализации !!!
    @property  # getter -> для того чтобы получить доступ к приватному полю
    def name(self):
        return self.__name

    @name.setter  # setter -> для того чтобы получить доступ к приватному полю и изменить его значение
    def name(self, username):
        if 1 < len(username) < 30:
            self.__name = username
        else:
            print("Incorrect name length!")

    @property  # getter -> для того чтобы получить доступ к приватному полю
    def age(self):
        return self.__age

    @age.setter  # setter -> для того чтобы получить доступ к приватному полю и изменить его значение
    def age(self, age):
        if 18 <= age < 150:
            self.__age = age
        else:
            print("Incorrect age!")

    def show_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}, Hobby: {self.hobby}")

    def __get_hobby(self):  # private method
        print("Hobby: " + self.hobby)


# vasya = User("", -20, "work")
# vasya.show_info()
# print(vasya.hobby)
# vasya.hobby = "nothing"
# print(vasya.hobby)
# # v1
# # vasya.set_age(45)
# # print(vasya.get_age())
# # vasya.show_info()
# # vasya.set_age(450)
# # vasya.show_info()
# # v2
# print(vasya.name)
# vasya.name = "Petya"
# vasya.show_info()
# vasya.name = ""
# vasya.show_info()

# print(vasya.__age)
#####
# vasya.__age = -33  # динамічно створилося нове поле в цьому экземплярi, але це поле не має жодного відношення до
# приватного поля __фпу яке ми створили у класі
# print(vasya.__age)
# vasya.show_info()
####
# vasya.__get_hobby()
# vasya._User__get_hobby()  # так робити не треба так як це ламає інкапсуляцію

######################
class MyConverter:
    __money_sum = 0
    __uah_rate = 38.3
    __converter_direction = 1

    def __init__(self, input_money, covert_dir):
        self.money_sum = input_money
        self.converter_direction = covert_dir

    @property
    def money_sum(self):
        return self.__money_sum

    @money_sum.setter
    def money_sum(self, money):
        if 100 <= money <= 100000:
            self.__money_sum = money
        else:
            raise Exception("Provide correct money sum!")

    @property
    def converter_direction(self):
        return self.__converter_direction

    @converter_direction.setter
    def converter_direction(self, converter_dir):
        if converter_dir == 1 or converter_dir == 2:
            self.__converter_direction = converter_dir
        else:
            raise Exception("Provide correct converter direction: 1 or 2!")

    # readonly свойство
    @property
    def uah_rate(self):
        return self.__uah_rate

    def show_result(self):
        print(self.__get_money_result())

    def __get_money_result(self):
        match self.__converter_direction:
            case 1:
                return f"{self.__money_sum:.2f} UAH = {self.__get_usd_sum():.2f} USD"
            case 2:
                return f"{self.__money_sum:.2f} USD = {self.__get_uah_sum():.2f} UAH"
            case _:
                raise Exception("Incorrect converter direction!")

    def __get_uah_sum(self):
        return self.__money_sum * self.__uah_rate

    def __get_usd_sum(self):
        return self.__money_sum / self.__uah_rate


try:
    converter = MyConverter(5000, covert_dir=1)
    converter.show_result()
except Exception as error:
    print(error)

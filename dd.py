# class City:
#     def __init__(self, name, region, country, pop, postal_code, phone_code):
#         self.__name = name
#         self.__region = region
#         self.__country = country
#         self.__pop = pop
#         self.__postal_code = postal_code
#         self.__phone_code = phone_code
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def region(self):
#         return self.__region
#
#     @region.setter
#     def region(self, region):
#         self.__region = region
#
#     @property
#     def country(self):
#         return self.__country
#
#     @country.setter
#     def country(self, country):
#         self.__country = country
#
#     @property
#     def pop(self):
#         return self.__pop
#
#     @pop.setter
#     def pop(self, pop):
#         self.__pop = pop
#
#     @property
#     def postal_code(self):
#         return self.__postal_code
#
#     @postal_code.setter
#     def postal_code(self, postal_code):
#         self.__postal_code = postal_code
#
#     @property
#     def phone_code(self):
#         return self.__phone_code
#
#     @phone_code.setter
#     def phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
# city_info = City("Київ", "Київська", "Україна", 2800000, "01000", "+380")
#
# print("Назва міста:", city_info.name)
# print("Регіон:", city_info.region)
# print("Країна:", city_info.country)
# print("Кількість жителів:", city_info.pop)
# print("Поштовий індекс:", city_info.postal_code)
# print("Телефонний код:", city_info.phone_code)

################################################################################################

# class Country:
#     def __init__(self, name, continent, population, phone_code, capital, cities):
#         self.__name = name
#         self.__continent = continent
#         self.__population = population
#         self.__phone_code = phone_code
#         self.__capital = capital
#         self.__cities = cities
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def continent(self):
#         return self.__continent
#
#     @continent.setter
#     def continent(self, continent):
#         self.__continent = continent
#
#     @property
#     def population(self):
#         return self.__population
#
#     @population.setter
#     def population(self, population):
#         self.__population = population
#
#     @property
#     def phone_code(self):
#         return self.__phone_code
#
#     @phone_code.setter
#     def phone_code(self, phone_code):
#         self.__phone_code = phone_code
#
#     @property
#     def capital(self):
#         return self.__capital
#
#     @capital.setter
#     def capital(self, capital):
#         self.__capital = capital
#
#     @property
#     def cities(self):
#         return self.__cities
#
#     @cities.setter
#     def cities(self, cities):
#         self.__cities = cities
#
# ukraine = Country("Україна", "Європа", 41000000, "+380", "Київ", ["Львів", "Харків", "Одеса", "Дніпро", "Запоріжжя"])
#
# print("Назва країни:", ukraine.name)
# print("Континент:", ukraine.continent)
# print("Кількість жителів:", ukraine.population)
# print("Телефонний код:", ukraine.phone_code)
# print("Столиця:", ukraine.capital)
# print("Міста:", ukraine.cities)
#


class Product:
    def __init__(self, description, brand, section, user):
        self.__description = description
        self.__brand = brand
        self.__section = section
        self.__user = user

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def section(self):
        return self.__section

    @section.setter
    def section(self, section):
        self.__section = section

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

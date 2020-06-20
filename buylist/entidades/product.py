class Product:
    def __init__(self, description, brand, user):
        self.__description = description
        self.__brand = brand
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
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

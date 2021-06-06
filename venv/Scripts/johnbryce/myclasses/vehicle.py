class __Vehicle:
    __max_speed: int
    __mileage: int
    __max_capacity: int

    def __init__(self, max_speed=100, mileage=0):
        self.__max_speed = max_speed
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed: int):
        self.__max_speed = max_speed


class Bus(__Vehicle):
    def __init__(self):
        super(Bus, self).__init__()



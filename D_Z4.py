class Clock:
    __DAY = 86400

    @staticmethod
    def arithmetic_error(value):
        if not isinstance(value, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")

    @staticmethod
    def zero_division_error(value):
        if value == 0:
            raise ZeroDivisionError("Нельзя делить на ноль")

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __init__(self, sec):
        if not isinstance(sec, int):
            raise TypeError("Секунды должны быть целым числом")
        if sec < 0:
            raise ValueError("Значение для секунд не может быть отрицательным")
        self.sec = sec % Clock.__DAY

    def __add__(self, other):
        Clock.arithmetic_error(other)
        return Clock(self.sec + other.sec)

    def __sub__(self, other):
        Clock.arithmetic_error(other)
        return Clock(self.sec - other.sec)

    def __mul__(self, other):
        Clock.arithmetic_error(other)
        return Clock(self.sec * other.sec)

    def __truediv__(self, other):
        Clock.arithmetic_error(other)
        Clock.zero_division_error(other.sec)
        return Clock(self.sec / other.sec)

    def __floordiv__(self, other):
        Clock.arithmetic_error(other)
        Clock.zero_division_error(other.sec)
        return Clock(self.sec // other.sec)

    def __mod__(self, other):
        Clock.arithmetic_error(other)
        Clock.zero_division_error(other.sec)
        return Clock(self.sec % other.sec)

    def __str__(self):
        return f"{self.get_format_time()}"

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise TypeError("Ключ должен быть строкой")
        if item == "hour":
            return (self.sec // 3600) % 24
        if item == "min":
            return (self.sec // 60) % 60
        if item == "sec":
            return self.sec % 60
        return "Некорректный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("Ключ должен быть строкой")
        if not isinstance(value, int) or value < 0:
            raise ValueError("Значение должно быть целым и положительным числом")
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        if key == "hour":
            self.sec = s + 60 * m + value * 3600
        if key == "min":
            self.sec = s + 60 * value + h * 3600
        if key == "sec":
            self.sec = value + 60 * m + h * 3600

    def __eq__(self, other):
        Clock.arithmetic_error(other)
        return self.sec == other.sec

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        Clock.arithmetic_error(other)
        return self.sec < other.sec

    def __le__(self, other):
        Clock.arithmetic_error(other)
        return self.sec <= other.sec

    def __gt__(self, other):
        Clock.arithmetic_error(other)
        return self.sec > other.sec

    def __ge__(self, other):
        Clock.arithmetic_error(other)
        return self.sec >= other.sec

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 60
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"


c1 = Clock(600)
c2 = Clock(200)
c3 = Clock(650)
print("c1:", c1)
print("c1 - c2:", c1 - c2)
print("c1 * c2:", c1 * c2)
print("c1 // c2:", c1 // c2)
print("c1 % c2:", c1 % c2)
c1 -= c2
print("c1 -= c2:", c1)
c1 *= c2
print("c1 *= c2:", c1)
c1 //= c2
print("c1 // c2:", c1)
print("c1 % c2:", c1 % c2)
print("c3 > c1", c3 > c1)
print("c3 >= c1", c3 >= c1)
print("c3 < c1", c3 < c1)
print("c3 <= c1", c3 <= c1)
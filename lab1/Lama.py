from Animal import Animal
class Lama(Animal):
    def __init__(self, continent, color, max_speed, symbol):
        super().__init__(continent, color)
        self.name = "Lama"
        self._max_speed = max_speed
        self._symbol = symbol
    def __repr__(self):
        return f'Animal(name = {self.name}, continent = {self._continent}, color = {self._color}, max_speed = {self._max_speed}, symbol = {self._symbol}'

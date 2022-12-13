from Animal import Animal
class Cheetah(Animal):
    def __init__(self, continent, color, max_speed, weight):
        super().__init__(continent, color)
        self.name = "Cheetah"
        self._max_speed = max_speed
        self._weight = weight
    def __repr__(self):
        return f'Animal(name = {self.name}, continent = {self._continent}, color = {self._color}, max_speed = {self._max_speed}, weight = {self._weight}'
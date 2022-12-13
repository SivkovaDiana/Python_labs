form Animal import Animal
class Penguin(Animal):
    def __init__(self, continent, color, max_speed, food):
        super().__init__(continent, color)
        self.name = "Penguin"
        self._max_speed = max_speed
        self._food = food
    def __repr__(self):
        return f'Animal(name = {self.name}, continent = {self._continent}, color = {self._color}, max_speed = {self._max_speed}, food = {self._food}'
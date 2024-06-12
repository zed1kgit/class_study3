class Figure:
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, a_side: int, b_side: int):
        self.a_side = a_side
        self.b_side = b_side

    def area(self):
        return self.a_side * self.b_side

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return (f"Прямоугольник у которого:\n"
                f"Первая сторона  = {self.a_side}\n"
                f"Вторая сторона = {self.b_side}")



class Circle(Figure):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return (f"Круг у которого:\n"
                f"Радиус  = {self.radius}")


class RightTriangle(Figure):
    def __init__(self, side: int, height: int):
        self.side = side
        self.height = height

    def area(self):
        return 0.5 * self.side * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return (f"Прямоугольный треугольник у которого:\n"
                f"Основание  = {self.side}\n"
                f"Высота = {self.height}")


class Trapezoid(Figure):
    def __init__(self, upside: int, downside: int, height: int):
        self.upside = upside
        self.downside = downside
        self.height = height

    def area(self):
        return 0.5 * (self.upside + self.downside) * self.height

    def __int__(self):
        return int(self.area())

    def __str__(self):
        return (f"Трапеция у которой:\n"
                f"Верхняя сторона = {self.upside}\n"
                f"Нижняя сторона = {self.downside}\n"
                f"Высота = {self.height}")

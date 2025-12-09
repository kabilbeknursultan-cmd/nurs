# task3_factory/shape_factory.py
from abc import ABC, abstractmethod


# 1. Негізгі Продукт Класы
class Shape(ABC):
    """Барлық фигураларға арналған базалық интерфейс."""

    @abstractmethod
    def draw(self):
        pass


# 2. Нақты Продуктылар
class Circle(Shape):
    def draw(self):
        print("Дөңгелек сызылды: Тұйықталған шеңбер")


class Rectangle(Shape):
    def draw(self):
        print("Тіктөртбұрыш сызылды: Төрт бұрыш, қарама-қарсы қабырғалары тең")


class Triangle(Shape):
    def draw(self):
        print("Үшбұрыш сызылды: Үш қабырғалы фигура")


# 5. Жүйенің кеңейтілуін көрсету үшін жаңа класс
class Square(Shape):
    def draw(self):
        print("Квадрат сызылды: Барлық қабырғалары тең төртбұрыш")


# 3. Фабрика Класы
class ShapeFactory:
    """Таңдалған түрге негізделген фигура нысандарын жасайды."""

    def create_shape(self, shape_type: str) -> Shape:
        """Сәйкес Shape нысанын қайтарады."""
        shape_type = shape_type.lower()

        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "triangle":
            return Triangle()
        # 5. Жаңа түрді қосу, бұл бар класс логикасын өзгертпейді
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Белгісіз фигура түрі: {shape_type}")


# --- Демонстрация ---
if __name__ == "__main__":
    print("### Тапсырма 3: Factory үлгісін тексеру ###")

    factory = ShapeFactory()

    # 4. Мысалдар: Фабриканы пайдалану

    print("\n--- Түр 1: Circle ---")
    try:
        circle = factory.create_shape("Circle")
        circle.draw()
    except ValueError as e:
        print(e)

    print("\n--- Түр 2: Rectangle ---")
    try:
        rectangle = factory.create_shape("rectangle")
        rectangle.draw()
    except ValueError as e:
        print(e)

    # Кеңейтілген түрді тексеру
    print("\n--- Түр 3: Square (Жаңа Продукт) ---")
    try:
        square = factory.create_shape("square")
        square.draw()
    except ValueError as e:
        print(e)
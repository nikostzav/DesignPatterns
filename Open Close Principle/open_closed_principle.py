
class Shape:
    def draw(self):
        raise NotImplementedError("You need to implement the draw method")


class Circle(Shape):
    def draw(self):
        print("Drawing a circle")


class Square(Shape):
    def draw(self):
        print("Drawing a square")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")


class ShapeDrawer:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):  
            self.shapes.append(shape)

    def draw_all(self):
        for shape in self.shapes:
            shape.draw()


if __name__ == "__main__": 
    drawer = ShapeDrawer()

    circle = Circle()
    square = Square()
    triangle = Triangle()

    drawer.add_shape(circle)
    drawer.add_shape(square)
    drawer.add_shape(triangle)

    drawer.draw_all()

from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'lines'


class RasterRenderer(Renderer):
    @property
    def what_to_render_as(self):
        return 'pixels'

class Shape:
    def __init__(self, renderer, name):
        self.renderer = renderer
        self.name = name

    def __str__(self):
        return f'Drawing {self.name} as {self.renderer.what_to_render_as}'

class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Triangle')


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer, 'Square')


if __name__ == '__main__':
    raster = RasterRenderer()
    triangle = Triangle(raster)
    print(triangle)

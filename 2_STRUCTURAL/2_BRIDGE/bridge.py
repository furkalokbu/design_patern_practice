from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass
    # def render_square

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Draving a circle of radius {radius}')

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Draving pixels for a circle of radius {radius}')


"""
wonderful
"""
from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line

DIAM = 10
COLOR = tuple

def make_ellipse(x, y, d):
    """
    helper function to make ellipses to pass to methods
    touch up and down
    """
    return Ellipse(pos=(x - d / 2, y - d / 2), size=(d, d))
    

class MyPainWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(), 1., 1.)
        with self.canvas:
            COLOR = Color(*color, mode='hsv')          
            make_ellipse(touch.x, touch.y, DIAM)
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

    def on_touch_up(self, touch):
        with self.canvas:
            COLOR
            make_ellipse(touch.x, touch.y, DIAM)


class MyPaintApp(App):
    def build(self):
        return MyPainWidget()

if __name__ == '__main__':
    MyPaintApp().run()
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.properties import NumericProperty, ObjectProperty


class MenuScreen(Screen):
    pass
class PlayerMenu(Widget):
    angle = NumericProperty(0)
    taille_blanc = NumericProperty(0)
    taille_dots = NumericProperty(1)
    def __init__(self, **kwargs):
        super(PlayerMenu, self).__init__(**kwargs)
        anim = Animation(taille_blanc=100)
        anim.start(self)
        anim = Animation(taille_dots=30)
        anim.start(self)
        anim = Animation(angle=360, duration=0) + Animation(angle=0, duration=3)
        anim.repeat = True
        anim.start(self)

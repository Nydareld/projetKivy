from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.metrics import dp
from .Bloc import Bloc
from kivy.uix.screenmanager import Screen

class Game(Screen):
    hmargin = NumericProperty(dp(10))
    vmargin = NumericProperty(dp(10))
    offset = NumericProperty(dp(100))
    startx = NumericProperty(dp(100))

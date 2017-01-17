from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.metrics import dp
from .Bloc import Bloc

class Board(Widget):
    hmargin = NumericProperty(dp(10))
    vmargin = NumericProperty(dp(10))

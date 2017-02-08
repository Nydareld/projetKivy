from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.metrics import dp
from .Bloc import Bloc
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from random import randint

class Game(Screen):
    # Offset entre chaque bloc
    offset = NumericProperty(dp(100))
    # marge avant le premier bloc
    startx = NumericProperty(dp(200))

    def __init__(self, **kwargs):
        Builder.load_file("duet/game/game.kv")

        super(Game, self).__init__(**kwargs)
        self.reset()

    def reset(self):
        for i in range(10):
            rand = randint(0, 10)
            print(rand)
            Bloc(i,50*rand,(200,30),self)

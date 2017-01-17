from kivy.app import App
from game import Game


class DuetApp(App):

    def on_pause(self):
        return True

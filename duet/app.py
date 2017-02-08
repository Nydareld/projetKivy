from kivy.app import App
from game import Game
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from .menu import MenuScreen, PlayerMenu
from .settings import SettingsScreen
from .level import LevelScreen



class DuetApp(App):

    def on_pause(self):
        return True

    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(Game(name='game'))
        self.sm.add_widget(LevelScreen(name='level'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        self.sm.current = 'menu'
        return self.sm

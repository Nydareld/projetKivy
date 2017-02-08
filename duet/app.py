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
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Game(name='game'))
        sm.add_widget(LevelScreen(name='level'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.current = 'menu'
        return sm

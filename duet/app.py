from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from .menu import MenuScreen
from .settings import SettingsScreen
from .game import GameScreen




class DuetApp(App):

    def on_pause(self):
        return True

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.current = 'menu'
        return sm

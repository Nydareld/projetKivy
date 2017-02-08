from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation
from kivy.metrics import dp
from kivy.animation import Animation

class Bloc(Widget):
    position = NumericProperty(0)
    positionLaterale = NumericProperty(dp(10))
    rgba = ObjectProperty((0.8,0.8,0.8,1))
    velocity_x = NumericProperty(3)

    #bouncy = NumericProperty(0)
    #rotation = NumericProperty(0)


    def __init__(self, position , positionLaterale,size, game):
        self.position = position
        self.positionLaterale = positionLaterale
        self.game = game
        self.size=size
        self.size_hint = None, None
        super(Bloc, self).__init__()
        self.game.add_widget(self)
        print('position : '+str(position))
        print('positionLaterale : '+str(positionLaterale))
        
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            print('position : '+str(self.position))
            print('positionLaterale : '+str(self.positionLaterale))
            print('width : '+str(self.width))
            print('height : '+str(self.height))
            return True

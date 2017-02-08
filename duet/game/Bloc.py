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
    angle = NumericProperty(0)
    #bouncy = NumericProperty(0)
    #rotation = NumericProperty(0)


    def __init__(self, position , positionLaterale,size,animations, game):
        self.position = position
        self.positionLaterale = positionLaterale
        self.game = game
        self.size=size
        self.animations = animations
        self.size_hint = None, None
        super(Bloc, self).__init__()
        self.game.add_widget(self)
        self.anim = Animation(y=-1000000 ,duration=3000)

    def move(self):
        self.anim.start(self)
        for animation in self.animations:
            getattr(self, 'animation%s' % animation)()

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            return True

    def animationRotation(self):
        animation = Animation(angle=360, duration=0) + Animation(angle=0, duration=3)
        animation.repeat = True
        animation.start(self)

    def animationBounce(self):
        animation = Animation(size=(self.size[0]+10,self.size[1]+10), t='in_quad') + Animation(size=(self.size[0]-20,self.size[1]-20), t='in_quad')
        animation.repeat = True
        animation.start(self)

    def animationSlide20(self):
        self.animationSlide(20)

    def animationSlide50(self):
        self.animationSlide(50)

    def animationSlide100(self):
        self.animationSlide(100)

    def animationSlide(self,slide=200):
        animation = Animation(x=self.pos[0]+slide)+Animation(x=self.pos[0]-slide)
        animation.repeat = True
        animation.start(self)

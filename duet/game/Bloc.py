from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty
from kivy.animation import Animation

class Bloc(Widget):
    width : NumericProperty(0)
    height : NumericProperty(0)
    position : NumericProperty(0)
    positionLaterale : NumericProperty(0)
    bouncy : NumericProperty(0)
    rotation : NumericProperty(0)

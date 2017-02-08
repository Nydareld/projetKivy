from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.metrics import dp
from .Bloc import Bloc
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from random import randint

class Game(Screen):
    # Offset entre chaque bloc
    offset = NumericProperty(dp(200))
    # marge avant le premier bloc
    startx = NumericProperty(dp(1000))
    blocs = []

    def __init__(self, **kwargs):
        Builder.load_file("duet/game/game.kv")

        super(Game, self).__init__(**kwargs)
        print("init")
        # self.reset()

    def reset(self,levelData=None):

        self.blocs = []

        if(levelData == None):
            for i in range(10):
                # 0--50<--->250--300<--->500--550<--->750--800
                gauche = [50,300,550]
                rand = randint(0, 2)
                bloc = Bloc(i,gauche[rand],(200,30),[],self)
                self.blocs.append(bloc)
        else :
            for blocData in levelData:
                index = blocData[0]
                yoffset = blocData[1]
                size = None
                if(len(blocData) > 2):
                    size = blocData[2]
                else:
                    size = (200,30)

                animations = None
                if(len(blocData) > 3):
                    animations = blocData[3]
                else:
                    animations = []

                bloc = Bloc(blocData[0],blocData[1],blocData[2],animations,self)
                self.blocs.append(bloc)

        for bloc in self.blocs:
            bloc.move()

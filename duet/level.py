from kivy.uix.screenmanager import Screen

class LevelScreen(Screen):

    levelData = [
        #lvl 1
        [
            [0,50,(200,30)],
            [1,50,(200,30)],
            [2,50,(200,30)],
            [3,50,(200,30)],

            [5,300,(200,30)],
            [6,300,(200,30)],
            [7,300,(200,30)],
            [8,300,(200,30)],

            [11,550,(200,30)],
            [12,550,(200,30)],
            [13,550,(200,30)],
            [14,550,(200,30)]
        ],
        #lvl 2
        [

        ],
        #lvl 3
        [

        ],
        #lvl 4
        [

        ],
        #lvl 5
        [

        ],
        #lvl 6
        [

        ],
        #lvl 7
        [

        ],
        #lvl 8
        [

        ],
        #lvl 9
        [

        ],
    ]

    # for blocData in levelData:
    #     bloc = Bloc(blocData[0],blocData[1],blocData[2],self)

    def play(self,lvlId):
        self.manager.current = 'game'
        game = self.manager.current_screen
        if(lvlId==0):
            game.reset()
        else:
            print(self.levelData[lvlId-1])
            game.reset(self.levelData[lvlId-1])

from ursina import *

#Made By Ido Chen


app = Ursina()
def input(key):
    global Score,Health
    if play.hovered:
        if key == 'left mouse down':
            MainMusic.play()
            MainMenu.disable()
            MainGame.enable()
    if RePlay.hovered:
        if key == 'left mouse down':
            Score = 0
            Health = 10
            Player.position = (0,0)
            MainMusic.resume()
            GameOver.disable()
            MainGame.enable()

    if Earth.hovered:
        if key == 'left mouse down':
            circileoflife.texture = 'assets\circile.png'
    if LavaPlanet.hovered:
        if key == 'left mouse down':
            circileoflife.texture = 'assets\Terran.png'
    if Ice.hovered:
        if key == 'left mouse down':
            circileoflife.texture = 'assets\Ice.png'
    if Baren.hovered:
        if key == 'left mouse down':
            circileoflife.texture = 'assets\Baren.png'


    if ExitOptions.hovered:
        if key == 'left mouse down':
            Options.disable()
            MainMenu.enable()
    if Options_Button.hovered:
        if key == 'left mouse down':
            Options.enable()
            MainMenu.disable()
def update():
    player_inter = Player.intersects()
    if MainGame.enabled == False:
        mouse.visible = True
        MainMusic.volume = 0
        Player.enabled = False
        square1.enabled = False
    if MainGame.enabled == True:
        mouse.visible = False
        MainMusic.volume = 0.4
        Player.enabled = True
        square1.enabled = True
    if GameOver.enabled == True:
        showscore.text='YOU LOST\nThe Score was: ' + str(int(Score))
    if Health <= 0:
        MainGame.disable()
        GameOver.enable()
    if player_inter.hit:
        if player_inter.entity == BorderUp or player_inter.entity == BorderDown or player_inter.entity == BorderLeft or player_inter.entity == BorderRight:
            MainGame.disable()
            GameOver.enable()

    if held_keys['s']:
        S.texture = 'assets\SPressd'
        S.y = -5.4
    if not held_keys['s']:
        S.y = -5
        S.texture = 'assets\S'
    if held_keys['a']:
        Abut.texture = 'assets\APressd'
        Abut.y = -5.4
    if not held_keys['a']:
        Abut.y = -5
        Abut.texture = 'assets\A'
    Score_OnScreen.text = str(int(Score))
    Health_OnScreen.text = 'Health: '+str(int(Health))


MainMenu = Entity(position = (0,0),enabled = True)
MainGame = Entity(position = (0,0),enabled = False)
GameOver = Entity(position = (0,0),enabled = False)
Options = Entity(position = (0,0),enabled = False)
Texture.default_filtering = None
#def update():
    #circileoflife_inter = circileoflife.intersects()
    #if circileoflife_inter.hit:
        #if circileoflife_inter.entity == square1:
        #circileoflife.color = color.red
class player(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.parent = MainGame
        self.scale = (0.8,0.8)
        self.position = (-0.2,0)
        self.collider = 'box'
        self.always_on_top = True
    def input(self,key):
        global Facing,moving
        if S.hovered:
            if key == 'left mouse down':
                moving += 1
        if Abut.hovered:
            if key == 'left mouse down':
                Facing += 1
        if key == 'a':
            Facing += 1
        if key == 's':
            moving += 1
    def update(self):
        global Facing,moving
        if Facing > 2:
            Facing = 1
        if moving > 2:
            moving = 1

        if Facing == 1:
            self.x += 2 * time.dt
            arrow.x = self.x + 0.4
        if Facing == 2:
            self.x -= 2 * time.dt
            arrow.x = self.x - 0.4
        if moving == 2:
            self.y += 2 * time.dt
            arrow.y = self.y + 0.4
            self.rotation_z -= 2
        if moving == 1:
            self.y -= 2 *time.dt
            arrow.y = self.y - 0.4
            self.rotation_z += 2

class EnemySqure(Entity):
    def __init__(self):
        super().__init__()
        self.model='quad'
        self.parent = MainGame
        self.scale = (1,1)
        self.position = (7, 0)
        self.collider = 'box'
    def update(self):
        global state,Score,Health

        #diffrent shooting postitions
        if state == 1:
            self.rotation_z = -90
            self.x -= 3 * time.dt
        if state == 2:
            self.x += 3 * time.dt
            self.rotation_z = 90
        if state == 3:
            self.y -= 3 * time.dt
            self.rotation_z = -180
        if state == 4:
            self.y += 3 * time.dt
            self.rotation_z = 0
        if state == 5:
            self.y += 3 * time.dt
            self.x -= 3 * time.dt
            self.rotation_z = -50
        if state == 6:
            self.y -= 3 * time.dt
            self.x += 3 * time.dt
            self.rotation_z = 130
        if state == 7:
            self.y += 3 * time.dt
            self.x += 3 * time.dt
            self.rotation_z = 50
        if state == 8:
            self.y -= 3 * time.dt
            self.x -= 3 * time.dt
            self.rotation_z = -130

        inter = self.intersects()
        if inter.hit:
            if inter.entity == Player or  inter.entity == circileoflife:
                self.disable()
                if self.enabled == False:
                    state = random.randrange(1,9)
                    if state == 1:
                        self.y = 0
                        self.x = 7
                    if state == 2:
                        self.y = 0
                        self.x = -7
                    if state == 3:
                        self.x = 0
                        self.y = 7
                    if state == 4:
                        self.x = 0
                        self.y = -7
                    if state == 5:
                        self.x = 7
                        self.y = -7
                    if state == 6:
                        self.x = -7
                        self.y = 7
                    if state == 7:
                        self.x = -7
                        self.y = -7
                    if state == 8:
                        self.x = 7
                        self.y = 7
                    invoke(self.enable,delay=1)
            if inter.entity == Player:
                Score += 1
                slash.play()

            if inter.entity == circileoflife:
                Health -= 1
                exp.play()
                circileoflife.color = color.red
                invoke(colorwhite,delay=0.4)

def colorwhite():
    circileoflife.color = color.white



#adjusting the window
window.title = 'Save The Planet By: Ido Chen'
window.borderless = True
window.size = (1000,900)
window.center_on_screen()
window.exit_button.enabled = False
window.fps_counter.enabled = False


# Facing vriable: 1 = Right, 2 = Left
Facing = 1
moving = 1


# postion of where the square shoots from
state = 1

# Main Menu buttous
play = Button(model = 'quad',scale = (3,1),color = color.white,position = (0,-1),parent = MainMenu,texture = 'assets\play.png')
exit = Button(model = 'quad',scale = (3,1),color = color.white,position = (0,-3),on_click = application.quit,parent = MainMenu,texture = 'assets\exit.png')
Options_Button = Button(model = 'quad',scale = (3.4,1),color = color.white,position = (0,-2),parent = MainMenu,texture = 'assets\options.png')
exitgame = Button(model = 'quad',scale = (1.5,1.5),color = color.white,position = (6,6),on_click = application.quit,parent = MainGame,texture = 'assets\exitgame.png')
headline = Entity(model = 'quad',position = (0,4),scale =(14,4),parent = MainMenu,texture = 'assets\headline.png')
tut = Text(text='Tip: "A" and "s" to change diraction',position = (-2.8,-4),parent = MainMenu,scale = (14,14))

# Game Over Screen
showscore = Text(text='YOU LOST\nThe Score was:',font = 'assets\space age.ttf',position = (-3,3),parent = GameOver,scale = (20,20))
ExitGame = Button(model='quad',scale = (3,1),position = (0,-3),color=color.white,on_click = application.quit,parent = GameOver,texture= 'assets\exit.png')
RePlay = Button(model='quad',scale = (3,1),position = (0,0),color=color.white,parent = GameOver,texture= 'assets\play.png')


# score and health
Score = 0
Health = 10
Score_OnScreen = Text(text=0,font = 'assets\space age.ttf',position = (-0.3,5),parent = MainGame,scale = (20,20))
Health_OnScreen = Text(text=0,font = 'assets\space age.ttf',color=color.red,position = (-7,6),parent = MainGame,scale = (20,20))

# options
Earth = Button(model='quad',scale = (1.5,1.5),position = (-1,0),color=color.white,parent = Options,texture='assets\circile.png')
LavaPlanet = Button(model='quad',scale = (1.5,1.5),position = (1,0),color=color.white,parent = Options,texture= 'assets\Terran.png')
Ice = Button(model='quad',scale = (1.5,1.5),position = (3,0),color=color.white,parent = Options,texture= 'assets\Ice.png')
Baren = Button(model='quad',scale = (1.5,1.5),position = (-3,0),color=color.white,parent = Options,texture= 'assets\Baren.png')
ExitOptions = Button(model='quad',scale = (3,1),position = (0,-3),color=color.white,parent = Options,texture= 'assets\exit.png')

# Main Game
Player = player()
arrow = Entity(model = 'quad',position = (0,0),color = color.red,scale =(0.1,0.1),parent = MainGame)
Player.texture = 'assets\shur.png'
exp = Audio('assets\exp.wav',loop=False,pitch = 2, autoplay=False)
slash = Audio('assets\swing.wav',loop=False,pitch = 1.5, autoplay=False)
MainMusic = Audio('assets\mainmusic.wav',parent = MainGame,loop=True, autoplay=False)
MainMusic.volume = 0.4
square1 = EnemySqure()
square1.texture = 'assets\\rocket.png'
BorderUp = Entity(model = 'quad',position = (0,6.5),color = color.white,scale =(15,0.5),collider = 'box',visible = False,parent = MainGame)
BorderDown =  duplicate(BorderUp,position = (0,-6.5))
BorderLeft =  duplicate(BorderUp,position = (-7.5,0),scale=(0.5,15))
BorderRight =  duplicate(BorderUp,position = (7.5,0),scale=(0.5,15))
S = Button(model = 'quad',position = (-4,-5),color = color.white,scale =(1.5,1.5),collider = 'box',texture='assets\S',visible = True,parent = MainGame)
Abut = Button(model = 'quad',position = (-6,-5),color = color.white,scale =(1.5,1.5),collider = 'box',texture='assets\A',visible = True,parent = MainGame)
circileoflife = Entity(model = 'quad',position = (0,0),color = color.white,scale =(2,2),collider = 'box',parent = MainGame,texture = 'assets\circile.png')
bg = Entity(model = 'quad',texture = 'assets\\bg.png',scale =(16,16),z = .1)

app.run()
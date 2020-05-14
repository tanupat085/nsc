from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

from real import *
from real2 import *
from real3 import *

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(dir_path + '/start.kv')

class Stage(Screen):
    
    def update(self,dt):
        pass
    
    def on_enter(self):
        print("Enter ")

        self.clock = Clock.schedule_interval(self.update, 1.0/60.0)


    def on_pre_leave(self):
        print("Leave")

        if self.clock:
            self.clock.cancel()
class S1(Stage):
    pass
class S2(Stage):
    pass

class StartPage(Stage):
    music = ObjectProperty(None)
    sound1 = SoundLoader.load("music2.wav")
    
    def update(self,dt):

        self.music = self.music

        if self.music.on == False :
            self.sound1.play()
            self.sound1.volume = 0.5
        else :
            self.sound1.stop()
            self.sound1.volume = 0.5



class Selectionpage(Stage):
    butt1 = ObjectProperty(None)
    butt2 = ObjectProperty(None)
    butt3 = ObjectProperty(None)
    buttback = ObjectProperty(None)
    play = ObjectProperty(None)
    
    def update(self,dt):
        
        self.buttback.image.source = "realback.png"
        
        self.butt1.image.source = "realstage1.png"
        self.butt2.image.source = "realstage2.png"
        self.butt3.image.source = "realstage3.png"
        

class MusicButt(Button):
    on = False
    def on_press(self):
        self.on = not self.on
        print('asdf')

class StageButton(Button):
    on = False
    def on_press(self):
        self.on = True

class StageButton_back(Button):
    on = False
    def on_press(self):
        self.on = True
class StageButton_go(Button):
    on = False
    def on_press(self):
        self.on = True


class RecommendPage(Stage):
    def update(self,dt):
        pass
    
    

class StageManager(ScreenManager):
    pass

class FirstStage(Stage):
    stage1 =ObjectProperty(None)
    def update(self,dt):
        self.stage1.update()


class SecondStage(Stage):
    stage2 = ObjectProperty(None)
    def update(self,dt):
        self.stage2.update()
    

class ThirdStage(Stage):
    stage3 = ObjectProperty(None)
    def update(self,dt):
        self.stage3.update()
    


class Helppage1(Stage):
    help1 = ObjectProperty(None)

class Helppage2(Stage):
    help2 = ObjectProperty(None)

class Helppage3(Stage):
    help3 = ObjectProperty(None)

class Helppage4(Stage):
    help4 = ObjectProperty(None)

class Helppage5(Stage):
    help5 = ObjectProperty(None)

class Helppage6(Stage):
    help6 = ObjectProperty(None)

class Helppage7(Stage):
    help7 = ObjectProperty(None)

class helpme(App):
    def build(self):
        stage_manager = StageManager()
        return stage_manager

if __name__ == '__main__':
    helpme().run()

import kivy
kivy.require('1.11.1') 
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider

import os
_path = os.path.dirname(os.path.realpath(__file__))
from Environment import *

class Page(App):

    def build(self):
        self.env = Environment()
        self.current_play_btn_image = self._get_play_image()
        layout = GridLayout(width=50, cols=1, size_hint=(0.25, 1))

        buttonLayout = GridLayout(rows=1)
        playButton = Button(size_hint=(None, None), size=(50, 50), background_color=[255,0,0,1], background_normal=self.current_play_btn_image, background_down=self.current_play_btn_image)
        playButton.bind(on_release=lambda x:self.playButtonChange())
        nextButtonImage = os.path.join(_path, "assets/next-button.png")
        nextButton = Button(size_hint=(None, None), size=(50, 50), background_color=[0,0,0,1], background_normal=nextButtonImage, background_down=nextButtonImage)
        nextButton.bind(on_release=lambda x:self.onNextButtonPress())
        buttonLayout.add_widget(playButton)
        buttonLayout.add_widget(nextButton)
        layout.add_widget(buttonLayout)

        sizeInputLabel = Label(text='Taille de la carte')
        initSizeInput = Slider(min=1, max=100, step=1, value=self.env.sizeOfMap, orientation='horizontal')
        initSizeInput.bind(value=lambda instance, value:self.env.sizeMap(instance, value))
        layout.add_widget(sizeInputLabel)
        layout.add_widget(initSizeInput)
        numberOfTypeLabel = Label(text='Nombre d\'éléments')
        numberOfTypeInput = Slider(min=3, max=10, step=1, value=self.env.numberOfType, orientation='horizontal')
        numberOfTypeInput.bind(value=lambda instance, value:self.env.changeNumberOfType(instance, value))
        layout.add_widget(numberOfTypeLabel)
        layout.add_widget(numberOfTypeInput)
        boutonInit = Button(text='Initialiser')
        boutonInit.bind(on_press=lambda x:self.initNew())
        layout.add_widget(boutonInit)
        root = BoxLayout(orientation='horizontal')
        root.add_widget(self.env)
        root.add_widget(layout)
        return root

    def initNew(self):
        self.env.initNewMap()

    def playButtonChange(self):
        if self.env.state == 'play':
            self.env.state = 'pause'
        else:
            self.env.state = 'play'
        self.current_play_btn_image = self._get_play_image()
    
    def onNextButtonPress(self):
        if self.env.state == 'pause':
            print("next")

    def _get_play_image(self):
        if self.env.state == 'play':
            return os.path.join(_path, "assets/pause-button.png")
        else:
            return os.path.join(_path, "assets/play-button.png")
            

if __name__ == '__main__':
    Page().run()
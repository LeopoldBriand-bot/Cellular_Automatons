import kivy
kivy.require('1.11.1') 
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from Environment import *

class Page(App):

    def build(self):
        self.env = Environment()
        layout = GridLayout(width=50, cols=2, size_hint=(0.25, 1))

        cohesionLabel = Label(text='Cohesion: ')
        layout.add_widget(cohesionLabel)
        checkboxCohesion = CheckBox()
        checkboxCohesion.bind(active = self.onCheckboxCohesionActive)
        layout.add_widget(checkboxCohesion)

        separationLabel = Label(text='Separation: ')
        layout.add_widget(separationLabel)
        checkboxSeparation = CheckBox()
        checkboxSeparation.bind(active = self.onCheckboxSeparationActive)
        layout.add_widget(checkboxSeparation)

        alignmentLabel = Label(text='Alignment: ')
        layout.add_widget(alignmentLabel)
        checkboxAlignment = CheckBox()
        checkboxAlignment.bind(active = self.onCheckboxAlignmentActive)
        layout.add_widget(checkboxAlignment)

        fieldOfViewLabel = Label(text='Field of view: ')
        layout.add_widget(fieldOfViewLabel)
        checkboxFieldOfView = CheckBox()
        checkboxFieldOfView.bind(active = self.onCheckboxFieldOfViewActive)
        layout.add_widget(checkboxFieldOfView)

        root = BoxLayout(orientation='horizontal')
        root.add_widget(self.env)
        root.add_widget(layout)
        return root

    def onCheckboxCohesionActive(self, checkbox, value):
        if value:
            self.env.params["cohesionEnabled"] = True
        else:
            self.env.params["cohesionEnabled"] = False
    
    def onCheckboxSeparationActive(self, checkbox, value):
        if value:
            self.env.params["separationEnabled"] = True
        else:
            self.env.params["separationEnabled"] = False

    def onCheckboxAlignmentActive(self, checkbox, value):
        if value:
            self.env.params["alignmentEnabled"] = True
        else:
            self.env.params["alignmentEnabled"] = False

    def onCheckboxFieldOfViewActive(self, checkbox, value):
        if value:
            self.env.params["nearBoidsDistanceEnabled"] = True
        else:
            self.env.params["nearBoidsDistanceEnabled"] = False

            

if __name__ == '__main__':
    Page().run()
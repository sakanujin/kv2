from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
#added below for making rounded button
from kivy.graphics import Color, RoundedRectangle
#added below for using toggle button
from kivy.uix.togglebutton import ToggleButton
#give class the name of Otameshi 
class Otameshi(BoxLayout):
    pass
#give class the name of ButtontestApp 
class Buttontest3App(App):
    def __init__(self, **kwargs):
        super(Buttontest3App, self).__init__(**kwargs)
    def build(self):
        return Otameshi()
if __name__ == '__main__':
    Buttontest3App().run()

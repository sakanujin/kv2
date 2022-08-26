from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


#give class the name of Otameshi 
class Otameshi(BoxLayout):
    pass

#give class the name of ButtontestApp 
class ButtontestApp(App):
    def __init__(self, **kwargs):
        super(ButtontestApp, self).__init__(**kwargs)

    def build(self):
        return Otameshi()

if __name__ == '__main__':
    ButtontestApp().run()

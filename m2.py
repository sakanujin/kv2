# %load ../0_Hello/main.py
from kivy.app import App
#from kivy.uix.label import Label

class TestApp(App):

    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'greeting'

if __name__ == "__main__":
    TestApp().run()

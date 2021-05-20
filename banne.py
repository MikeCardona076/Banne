from kivy.uix.button import Button

from kivy.app import App

from functools import partial
import time
from kivy.uix.button import Label



class Banne(App):

    def disable(self, instance, *args):

        instance.disabled = True

    def update(self, instance, *args):

        instance.text = time.ctime()
        

    def build(self):

        mybtn = Button(text="Bienvenida de nuevo Banne!!!", font_size='30')

        mybtn.bind(on_press=partial(self.disable, mybtn))

        mybtn.bind(on_press=partial(self.update, mybtn))

        return mybtn

Banne().run()
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import time
import requests
from kivy.core.text import Label as CoreLabel
from kivy.core.image import Image 
from kivy.uix.image import AsyncImage


class Banne(App):

    def build(self):

        layout = GridLayout(cols=2)
        layout.add_widget(Button(text=time.ctime()))

        layout.add_widget(Button(text="Enviar ubicación a Mike"))

        return layout


if __name__ == '__main__':
    Banne().run()
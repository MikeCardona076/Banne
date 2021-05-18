import kivy
from kivy.app import App
from kivy.uix.image import AsyncImage
from kivy.uix.carousel import Carousel



# Create the App class
class CarouselApp(App):
	def build(self):
		carousel = Carousel(direction ='right')
		src ="https://static2.abc.es/media/tecnologia/2019/08/01/cara-kld--1200x630@abc.jpg"
		image = AsyncImage(source = src, allow_stretch = True)
		carousel.add_widget(image)


		return carousel

CarouselApp().run()
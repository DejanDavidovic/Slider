from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Circlelayout(BoxLayout):
    pass


class CircleApp(App):
    def build(self):
        return Circlelayout()


CircleApp().run()













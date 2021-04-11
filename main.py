from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class Work(FloatLayout):
    pass


class My_AppApp(App):
    def build(self):
        return Work()


if __name__ == '__main__':
    My_AppApp().run()

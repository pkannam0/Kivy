from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Work(GridLayout):
        pass

class My_App(App):
    def build(self):
        return Work()

if __name__ == '__main__':
    My_App().run()
from kivymd.app import MDApp
from kivy.lang import Builder

<<<<<<< HEAD
=======

class Work(FloatLayout):
    pass

>>>>>>> 79a7f18507cb6e4d9b6d1d7982f5f6488af30563

class My_AppApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("my_app.kv")



if __name__ == '__main__':
    My_AppApp().run()

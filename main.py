from kivymd.app import MDApp
from kivy.lang import Builder


class My_AppApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("my_app.kv")
    
    def sign_up(self):
        self.root.ids.email.text = ""
        self.root.ids.password.text = ""
        self.root.ids.welcome_label.text = f'Hey! Welcome to the LFL App'

    def login(self):
        self.root.ids.email.text = ""
        self.root.ids.password.text = ""
        self.root.ids.welcome_label.text = f'Welcome Back!'



if __name__ == '__main__':
    My_AppApp().run()

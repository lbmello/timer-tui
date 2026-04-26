from textual.app import App

from main_screen import MainMenu

class MyApp(App):

    def on_mount(self):
        self.push_screen(MainMenu())


if __name__ == "__main__":
    app = MyApp()
    app.run()

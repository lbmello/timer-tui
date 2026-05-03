from textual.app import App

from screens.main_menu import MainMenu
from screens.dual_timer import DualTimerScreen
from screens.time_timer import TimeTimerScreen


class MyApp(App):
    # Defina as telas aqui. O Textual as carrega "on demand"
    SCREENS = {
        "main": MainMenu,
        "dual": DualTimerScreen,
        "time": TimeTimerScreen,
    }

    def on_mount(self):
        self.push_screen("main")

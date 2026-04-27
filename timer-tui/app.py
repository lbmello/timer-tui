from textual.app import App

from screens.main_menu import MainMenu
from screens.dual_timer import DualTimerScreen
from screens.time_timer import TimeTimerScreen


class MyApp(App):
    def on_mount(self):
        self.main_menu = MainMenu()
        self.dual_timer = DualTimerScreen()
        self.time_timer = TimeTimerScreen()
    
        try:
            self.switch_screen(self.main_menu)
        except IndexError:
            self.main_menu.push_screen()
            self.main_menu.pop_screen()

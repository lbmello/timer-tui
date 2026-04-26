from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical


class MainMenu(Screen):

    def compose(self) -> ComposeResult:
        yield Static("Main Menu", id="title")

        with Vertical():
            yield Button("Dual Timers", id="go-dual")
            yield Button("Time Timer", id="go-time-timer")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "go-dual":
            from dual_timer import DualTimerScreen
            self.app.push_screen(DualTimerScreen())
        elif event.button.id == "go-time-timer":
            from time_timer import TimeTimerScreen
            self.app.push_screen(TimeTimerScreen())

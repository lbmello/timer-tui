from textual.screen import Screen
from textual.widgets import Button, Static
from textual.containers import Vertical


class MainMenu(Screen):

    def on_mount(self):
        self.query_one(Button).focus()

    def compose(self):
        yield Static("Main Menu", id="title")

        with Vertical():
            yield Button("Dual Timers", id="go-dual")
            yield Button("Time Timer", id="go-time-timer")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        app = self.app

        match event.button.id:
            case "go-dual":
                app.switch_screen("dual")

            case "go-time-timer":
                app.switch_screen("time")


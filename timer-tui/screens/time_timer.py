from textual.reactive import reactive
from textual.widgets import Static
from textual.screen import Screen
from textual.widgets import Button, Static, Header, Footer

import time

class TimeTimerScreen(Screen):

    remaining = reactive(0)
    total = reactive(0)

    def compose(self) -> ComposeResult:
        yield Header()

        self.timer_display = Static("Set time and start", id="time-display")
        yield self.timer_display

        yield Button("Start 5 min", id="start-5")
        yield Button("Start 10 min", id="start-10")

        # 🔴 Back button
        yield Button("← Back to Menu", id="back")

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()

        elif event.button.id == "start-5":
            self.start_timer(5)

        elif event.button.id == "start-10":
            self.start_timer(10)

    def start_timer(self, minutes: int):
        self.total = minutes * 60
        self.remaining = self.total
        self.set_interval(1, self.tick)

    def tick(self):
        if self.remaining <= 0:
            self.timer_display.update("⏰ Time's up!")
            return

        self.remaining -= 1

        percent = self.remaining / self.total
        bar_length = 30
        filled = int(bar_length * percent)

        bar = "█" * filled + "-" * (bar_length - filled)

        mins = self.remaining // 60
        secs = self.remaining % 60

        self.timer_display.update(f"{mins:02d}:{secs:02d}\n[{bar}]")

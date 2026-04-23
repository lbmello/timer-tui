from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer
import time
from pyfiglet import Figlet


class Timer:
    def __init__(self):
        self.running = False
        self.start_time = 0
        self.elapsed = 0
        self.laps = []


    def toggle(self):
        if self.running:
            self.elapsed += time.time() - self.start_time
            self.running = False
        else:
            self.start_time = time.time()
            self.running = True


    def lap(self):
        self.laps.append(self.get_time())

    def get_time(self):
        total = self.elapsed
        if self.running:
            total += time.time() - self.start_time

        total = int(total)
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return f"{h:02}:{m:02}:{s:02}"


class DualTimerApp(App):
    CSS_PATH = "style.tcss"


    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="body"):
            with Vertical(id="timer1-box"):
                self.timer1_display = Static(id="timer1")
                self.timer1_laps = Static(id="timer1-laps")
                yield self.timer1_display
                yield self.timer1_laps

                with Horizontal(id="lap-count"):
                    self.timer1_lap_count_display = Static(id="timer1-laps-count")
                    yield self.timer1_lap_count_display

            with Vertical(id="timer2-box"):
                self.timer2_display = Static(id="timer2")
                self.timer2_laps = Static(id="timer2-laps")
                yield self.timer2_display
                yield self.timer2_laps

                with Horizontal(id="lap-count"):
                    self.timer2_lap_count_display = Static(id="timer2-laps-count")
                    yield self.timer2_lap_count_display



        with Horizontal(id="controls"):
            yield Button("Work Start/Stop", id="t1-toggle")
            yield Button("Work Lap", id="t1-lap")
            yield Button("Personal Start/Stop", id="t2-toggle")
            yield Button("Personal Lap", id="t2-lap")

        yield Footer()


    def on_mount(self):
        self.timer1 = Timer()
        self.timer2 = Timer()

        self.figlet = Figlet(font="starwars")
        self.theme = "dracula"

        self.set_interval(1, self.update_times)


    def _ascii_time(self, label: str, value: str) -> str:
        safe_value = value.replace(":", " ")

        art = self.figlet.renderText(safe_value)

        lines = art.splitlines()
        max_width = min(60, self.size.width - 10)
        trimmed = "\n".join(line[:max_width] for line in lines)

        return f"{label}\n{trimmed}"


    def update_times(self):
        self.timer1_display.update(
            self._ascii_time("Work", self.timer1.get_time())
        )

        self.timer2_display.update(
            self._ascii_time("Personal", self.timer2.get_time())
        )

        self.timer1_laps.update(
            "\n".join(
                f"Lap {i+1}: {t} | Elapsed: {t}"
                for i, t in enumerate(self.timer1.laps)
            ) or "No laps"
        )

        self.timer2_laps.update(
            "\n".join(
                f"Lap {i+1}: {t} | Elapsed: {t}"
                for i, t in enumerate(self.timer2.laps)
            ) or "No laps"
        )

        self.timer1_lap_count_display.update(f'Total: {str(len(self.timer1.laps))}' or "0 laps")
        self.timer2_lap_count_display.update(f'Total: {str(len(self.timer2.laps))}' or "0 laps")



    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "t1-toggle":
                self.timer1.toggle()
            case "t1-lap":
                self.timer1.lap()
            case "t2-toggle":
                self.timer2.toggle()
            case "t2-lap":
                self.timer2.lap()


if __name__ == "__main__":
    DualTimerApp().run()
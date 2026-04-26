
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer
from pyfiglet import Figlet

from timer import timer as Timer

class tui_app(App):
    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="body"):
            with Vertical(id="timer_work-box"):
                self.timer_work_display = Static(id="timer_work")
                self.timer_work_laps = Static(id="timer_work-laps")
                yield self.timer_work_display
                yield self.timer_work_laps

                with Horizontal(id="lap-count"):
                    self.timer_work_lap_count_display = Static(id="timer_work-laps-count")
                    yield self.timer_work_lap_count_display

            with Vertical(id="timer_personal-box"):
                self.timer_personal_display = Static(id="timer_personal")
                self.timer_personal_laps = Static(id="timer_work-laps")
                yield self.timer_personal_display
                yield self.timer_personal_laps

                with Horizontal(id="lap-count"):
                    self.timer_personal_lap_count_display = Static(id="timer_personal-laps-count")
                    yield self.timer_personal_lap_count_display

        with Horizontal(id="controls"):
            yield Button("Work Start/Stop", id="t1-toggle")
            yield Button("Work Lap", id="t1-lap")
            yield Button("Personal Start/Stop", id="t2-toggle")
            yield Button("Personal Lap", id="t2-lap")

        yield Footer()


    def on_mount(self):
        self.timer_work = Timer()
        self.timer_personal = Timer()

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
        self.timer_work_display.update(
            self._ascii_time("Work", self.timer_work.get_time())
        )

        self.timer_personal_display.update(
            self._ascii_time("Personal", self.timer_personal.get_time())
        )

        self.timer_work_laps.update(
            "\n".join(
                f"Lap {i+1}: {t} | Elapsed: {t}"
                for i, t in enumerate(self.timer_work.laps)
            ) or "No laps"
        )

        self.timer_personal_laps.update(
            "\n".join(
                f"Lap {i+1}: {t} | Elapsed: {t}"
                for i, t in enumerate(self.timer_personal.laps)
            ) or "No laps"
        )

        self.timer_work_lap_count_display.update(f'Total: {str(len(self.timer_work.laps))}' or "0 laps")
        self.timer_personal_lap_count_display.update(f'Total: {str(len(self.timer_personal.laps))}' or "0 laps")


    def on_button_pressed(self, event: Button.Pressed):
        match event.button.id:
            case "t1-toggle":
                self.timer_work.toggle()
            case "t1-lap":
                self.timer_work.lap()
            case "t2-toggle":
                self.timer_personal.toggle()
            case "t2-lap":
                self.timer_personal.lap()


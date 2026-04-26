from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer
from pyfiglet import Figlet


from timer import timer
from tui_app import tui_app


if __name__ == "__main__":
    app = tui_app()
    app.run()

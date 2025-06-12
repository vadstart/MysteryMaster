from pathlib import Path

from rich import console
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual import events
from textual.widgets import RichLog
from textual.color import Color

class GameView(Static):
    def compose(self) -> ComposeResult:
        ascii_art = Path("art/coffee.txt").read_text()
        yield Static(ascii_art, id="ascii-art")

class InventoryPanel(Static):
    def compose(self) -> ComposeResult:
        inventory = "- Sword\n- Apple"
        yield Static(inventory, id="inventory-content")

class LogPanel(Static):
    # log_text = Content("> You wake up...\n> A noise comes from the hall...")

    def compose(self) -> ComposeResult:
        yield Static("Press 't' to change this text", id="text_widget")

    def append_log(self, message: str) -> None:
        # Find the widget by id
        text_widget = self.query_one("#text_widget", Static)
        # Update the text
        text_widget.update(f"\n> {message}")

class GameApp(App):
    CSS_PATH = "style.css"
    BINDINGS = [
        ("t", "npc_talk", "Talk with a Character"),
        ("q", "app_quit", "Quit the Game"),
    ]

    def compose(self) -> ComposeResult:
        self.game_view = GameView(id="game")
        self.inventory = InventoryPanel(id="inventory")
        self.log_panel = LogPanel(id="log")

        yield Vertical(
            Horizontal(
                self.game_view,
                self.inventory,
                id="top-half"
            ),
            self.log_panel,
            id="main"
        )

    def action_npc_talk(self) -> None:
        self.log_panel.append_log("You walk north.")
        print("You walk ..")

    def action_app_quit(self) -> None:
        self.exit()

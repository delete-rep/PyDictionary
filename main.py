import queue
import time
from pynput.keyboard  import Listener
from rich.live import Live
from rich.table import Table
from rich.layout import Layout
from rich.panel import Panel
from rich.padding import Padding
from rich.console import Console,Group


from core import Core

console = Console()

def make_layout() -> Layout:

    layout = Layout(name="root") 
    layout.split(
        Layout(name = "header",size =2),
        Layout(name="main", size = 3),
        Layout(name = "suggestion",size=3),
        
        Layout(name = "view",ratio=2),

    )

    return layout


layout = make_layout()
core = Core(layout= layout)

from rich.spinner import Spinner
layout["header"].update(Padding(pad=(0,70),renderable=Spinner(name="dots12")))
core.table =  Table(expand=True,show_edge=False)
core.table.add_column()
layout["view"].update(Padding(core.table,pad =(0,40),expand=True))


#listens for keyboard presses and 
with Listener(on_press= core.save_key) as L:

    with Live(layout, refresh_per_second=10):  # update 4 times a second to feel fluid
        #while the app hase not been terminated
        while core.running:
            layout["main"].update(Padding(Panel(core.formated_text),pad =(0,20)))
            layout["suggestion"].update(Padding(core.suggestion,pad =(0,20),expand=True))

    L.join()
from rich.console import Console
import time
console = Console()
with console.status("Monkeying around...", spinner="monkey"):
    for i in range(100):
        print(i)
        time.sleep(0.5)

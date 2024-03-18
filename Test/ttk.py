import ttkbootstrap as ttk
from typing import *

# Create window
window = ttk.Window(
    title="Main",  # title
    themename="morph",  # theme
    size=(500, 500),  # size
    resizable=(False, True),  # can be resize => (width, height)
    position=(300, 300),  # position
)
window.state("zoomed")
window.bind("<Escape>", lambda _: window.quit())

list_task: List[ttk.Entry] = []


def on_submit(entry: ttk.Entry) -> None:
    task = ttk.Label(master=window, text=f"Hello {entry.get()}", bootstyle="primary")
    task.pack(pady=10)
    list_task.append(task)


# Widgets
ttk.Style().configure("TLabel", bootstyle="success", font=("Arial", 15))
name = ttk.Label(master=window, text="Bào Ngư")
name.pack(padx=10, pady=10)
name.config(
    font=("Fira Code Retina", 20), text="AzureAbalone", bootstyle="inverse-danger"
)
entry_name = ttk.Entry(master=window, bootstyle="primary", font=("Cambria Math", 20))
entry_name.pack(pady=10, fill="x")
button = ttk.Button(
    master=window,
    text="heelo",
    bootstyle="primary",
    command=lambda entry=entry_name: on_submit(entry),
)
button.pack(side="left", expand=1, fill="both")
delete = ttk.Button(
    master=window,
    bootstyle="danger-outline",
    text="dangerous",
    command=lambda: [i.destroy() for i in list_task],
)
delete.pack(expand=1, side="right", fill="both")
# run
window.mainloop()

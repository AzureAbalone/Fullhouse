import ttkbootstrap as tb
from app.config.window_config import MAIN_WINDOW
from ttkbootstrap.toast import ToastNotification


class MainAppUI:
    def __init__(self) -> None:
        self.main_window = tb.Toplevel(**MAIN_WINDOW)
        self.main_window.bind("<Escape>", lambda _: self.main_window.quit())

        ## Main frame
        self.main_frame = tb.Frame(master=self.main_window)
        self.main_frame.pack(expand=1, fill="both")

        ## Header
        self.frame_header = tb.Frame(self.main_frame)
        self.frame_header.pack(padx=10, fill="x")

        ## Left-center-right child frame
        self.left_header = tb.Frame(self.frame_header)
        self.left_header.pack(side="left")
        self.center_header = tb.Frame(self.frame_header)
        self.center_header.pack(side="left", expand=1, fill="x")
        self.right_header = tb.Frame(self.frame_header)
        self.right_header.pack(side="right")
        self.implement_header()

    def implement_header(self) -> None:
        ## Right header frame
        self.mb_avatar = tb.Menubutton(
            self.right_header, text="Avatar", style="primary"
        )
        self.mb_avatar.pack(side="right", padx=10)
        ## Selection
        self.menu_func = tb.Menu(self.mb_avatar, tearoff=0)
        self.list_menu_avatar = ["Profile", "Setting", "Logout"]
        self.list_menu_func = [0, 0, self.close]
        for i, j in zip(self.list_menu_avatar, self.list_menu_func):
            self.menu_func.add_command(label=i, command=j)
        self.mb_avatar.config(menu=self.menu_func)

        ## Menu theme
        self.mb_theme = tb.Menubutton(self.right_header, text="Theme", style="primary")
        self.mb_theme.pack(side="right", padx=10)
        ## Selection
        self.menu_theme = tb.Menu(self.mb_theme, tearoff=0)
        self.list_menu_theme = self.main_window.style.theme_names()
        for i in self.list_menu_theme:
            self.menu_theme.add_command(
                label=i, command=lambda theme=i: self.main_window.style.theme_use(theme)
            )
        self.mb_theme.config(menu=self.menu_theme)

    def run(self) -> None:
        self.main_window.mainloop()

    def close(self) -> None:
        self.main_window.destroy()
        self.toast_bye = ToastNotification(
            title="", message=f"Goodbye!", bootstyle="light", duration="2000"
        )
        self.toast_bye.show_toast()

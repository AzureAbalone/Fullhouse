import ttkbootstrap as tb
from app.config.window_config import AUTH_WINDOW
from typing import *
from ttkbootstrap.toast import ToastNotification
from app.layout.mainapp_ui import MainAppUI
from app.db.crud import *
from app.db.database import session, User


class AuthUI:
    users = session.query(User)
    usernames = session.query(User.name).all()

    def __init__(self) -> None:
        self.main_window = tb.Window(**AUTH_WINDOW)
        self.main_window.bind("<Escape>", lambda _: self.main_window.quit())

        ## Style
        self.font = ("Fira Code Retina", 18)
        self.style = tb.Style()
        self.style.configure(".", font=self.font)

        ## Main frame: Largest frame, which has the same size as window, contains all widgets and child frames
        self.main_frame = tb.Frame(master=self.main_window)
        self.main_frame.pack(expand=True, fill="both", padx=10, pady=10)

        ## Create widget
        self.title = tb.Label(
            master=self.main_frame,
            text="Sign in",
        )
        self.title.pack(pady=40)

        ## Username: LabelFrame with Entry
        self.labelf_username = tb.LabelFrame(self.main_frame, text="Username")
        self.labelf_username.pack(padx=5, pady=5, fill="x")
        self.entry_username = tb.Entry(self.labelf_username, font=self.font)
        self.entry_username.pack(padx=5, pady=5, fill="x")

        ## Password: LabelFrame with Entry
        self.labelf_password = tb.LabelFrame(self.main_frame, text="Password")
        self.labelf_password.pack(padx=5, pady=5, fill="x")
        self.entry_password = tb.Entry(self.labelf_password, show="*", font=self.font)
        self.entry_password.pack(padx=5, pady=5, fill="x")

        ## Login and register
        self.frame_action = tb.Frame(self.main_frame)
        self.frame_action.pack(padx=5, pady=40)
        self.login_button = tb.Button(
            self.frame_action, text="Login", command=self.on_login
        )
        self.login_button.pack(side="left", padx=10)
        self.register_button = tb.Button(
            self.frame_action, text="Register", command=self.on_register
        )
        self.register_button.pack(side="right", padx=10)

    def on_login(self) -> None:
        if self.entry_username.get() in AuthUI.usernames:
            if (
                self.entry_password.get()
                == AuthUI.users.filter(User.name == self.entry_username.get())
                .first()
                .password
            ):
                self.toast_login_successfully = ToastNotification(
                    title="",
                    message=f"Hello {self.entry_username.get()}!",
                    bootstyle="success",
                    duration=2000,
                )
                self.toast_login_successfully.show_toast()

                ## Home
                MainAppUI().run()
            else:
                self.toast_login_failed = ToastNotification(
                    title="",
                    message="Wrong username or password!",
                    bootstyle="danger",
                    duration=2000,
                )
                self.toast_login_failed.show_toast()
        else:
            self.toast_nouser = ToastNotification(
                title="", message="INVALID user!", bootstyle="danger", duration=2000
            )
            self.toast_nouser.show_toast()

    def on_register(self) -> None:
        if self.entry_username.get() not in AuthUI.usernames:
            if self.entry_username.get() == "" or self.entry_password.get() == "":
                self.toast_register_failed = ToastNotification(
                    title="",
                    message="INVALID username or password!",
                    bootstyle="danger",
                    duration=3000,
                )
                self.toast_register_failed.show_toast()
            else:
                self.toast_register_success = ToastNotification(
                    title="",
                    message="Sucessfully registered!",
                    bootstyle="success",
                    duration=2500,
                )
                self.toast_register_success.show_toast()
                create(
                    name=self.entry_username.get(), password=self.entry_password.get()
                )
        else:
            self.toast_register_duplicate = ToastNotification(
                title="",
                message="Existed Usernames!",
                bootstyle="danger",
                duration=3000,
            )

    def run(self) -> None:
        self.main_window.mainloop()

    def close(self) -> None:
        self.main_window.destroy()

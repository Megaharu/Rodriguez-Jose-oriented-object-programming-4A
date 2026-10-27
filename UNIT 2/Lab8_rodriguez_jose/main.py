import tkinter as tk

from models.user_model import UserModel
from views.login_view import LoginView
from controlers.authentication import Authentication


class System:

    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = Authentication(self.modelo, self.vista)

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.iniciar()

import tkinter as tk
from tkinter import messagebox
from login_models import user

class login_window():
    def __init__(self, root):
        self.root = root
        self.root.title("inicio de sesion al sistema")
        self.root.geometr("300x300")
        self.root.resizable(False, False)

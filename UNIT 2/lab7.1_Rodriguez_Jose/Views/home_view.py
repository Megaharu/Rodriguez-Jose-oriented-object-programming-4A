import tkinter as tk
from tkinter import ttk, messagebox
from Models.products_model import Product

# Colores: verde, negro y oro
AZUL = "#18157F"
NEGRO_SUAVE = "#161616"
ROJO_VINO = "#6B0B16"
ROJO_ROSADO = "#A81F4D"
CELESTE = "#37CFD4"
CELESTE_CLARO = "#B8ECF5"


class DashboardVentana:
    def __init__(self, root, nombre_usuario):
        self.root = root
        self.nombre_usuario = nombre_usuario
        self.root.title("Panel Principal - Sistema")
        self.root.geometry("900x600")
        self.root.configure(bg=AZUL)

        self._configurar_estilos()
        self._crear_interfaz()
        self._cargar_productos()

    # ------------------------------------------------------------------
    # Estilos
    # ------------------------------------------------------------------
    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TFrame", background=AZUL)
        style.configure("TLabel", background=AZUL, foreground=CELESTE, font=("Helvetica", 11))
        style.configure("Titulo.TLabel", font=("Helvetica", 14, "bold"))

        style.configure("TLabelframe", background=AZUL, bordercolor=CELESTE)
        style.configure("TLabelframe.Label", background=AZUL, foreground=CELESTE,
                        font=("Helvetica", 10, "bold"))

        style.configure("TNotebook", background=AZUL, borderwidth=0)
        style.configure("TNotebook.Tab", background=NEGRO_SUAVE, foreground=CELESTE,
                        padding=(16, 6), font=("Helvetica", 11))
        style.map("TNotebook.Tab",
                  background=[("selected", ROJO_VINO)],
                  foreground=[("selected", CELESTE )])

        style.configure("TEntry", fieldbackground=NEGRO_SUAVE, foreground=CELESTE_CLARO,
                        insertcolor=CELESTE, bordercolor=CELESTE, lightcolor=CELESTE, darkcolor=CELESTE)
        style.map("TEntry", bordercolor=[("focus", CELESTE)], lightcolor=[("focus", CELESTE)],
                  darkcolor=[("focus", CELESTE)])

        style.configure("Treeview", background=NEGRO_SUAVE, fieldbackground=NEGRO_SUAVE,
                        foreground=CELESTE_CLARO, rowheight=26, bordercolor=CELESTE,
                        font=("Helvetica", 11))
        style.map("Treeview", background=[("selected", ROJO_VINO)],
                  foreground=[("selected", CELESTE)])
        style.configure("Treeview.Heading", background=ROJO_VINO, foreground=CELESTE,
                        relief="flat", font=("Helvetica", 10, "bold"))
        style.map("Treeview.Heading", background=[("active", ROJO_ROSADO)])

        style.configure("Guardar.TButton", background=ROJO_VINO, foreground=CELESTE,
                        bordercolor=CELESTE, padding=6, font=("Helvetica", 11, "bold"))
        style.map("Guardar.TButton",
                  background=[("active", ROJO_ROSADO)],
                  foreground=[("active", AZUL)])

    # ------------------------------------------------------------------
    # Interfaz
    # ------------------------------------------------------------------
    def _crear_interfaz(self):
        lbl_bienvenida = ttk.Label(
            self.root, text=f"Bienvenido/a, {self.nombre_usuario}", style="Titulo.TLabel"
        )
        lbl_bienvenida.pack(pady=(20, 15))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=30, pady=(0, 30))

        self.tab_inicio = ttk.Frame(self.notebook)
        self.tab_inventario = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_inicio, text="Inicio")
        self.notebook.add(self.tab_inventario, text="Inventario de Productos")

        self._crear_tab_inicio()
        self._crear_tab_inventario()

    def _crear_tab_inicio(self):
        lbl_tienda = ttk.Label(
            self.tab_inicio, text="Tienda de Videojuegos", style="Titulo.TLabel"
        )
        lbl_tienda.pack(pady=(80, 10))

        lbl_mensaje = ttk.Label(
            self.tab_inicio,
            text=f"¡Bienvenido/a al Sistema!\n\nUsuario activo:\n{self.nombre_usuario}",
            justify="center",
        )
        lbl_mensaje.pack()

    def _crear_tab_inventario(self):
        # ----- Formulario "Registrar Producto" -----
        frame_form = ttk.LabelFrame(self.tab_inventario, text="Registrar Producto", padding=10)
        frame_form.pack(side="left", fill="y", padx=(15, 10), pady=15)

        ttk.Label(frame_form, text="Nombre:").pack(anchor="w", pady=(5, 2))
        self.entry_nombre = ttk.Entry(frame_form, width=24)
        self.entry_nombre.pack(fill="x")

        ttk.Label(frame_form, text="Precio:").pack(anchor="w", pady=(18, 2))
        self.entry_precio = ttk.Entry(frame_form, width=24)
        self.entry_precio.pack(fill="x")

        ttk.Label(frame_form, text="Stock:").pack(anchor="w", pady=(18, 2))
        self.entry_stock = ttk.Entry(frame_form, width=24)
        self.entry_stock.pack(fill="x")

        btn_guardar = ttk.Button(
            frame_form, text="Guardar Producto", style="Guardar.TButton",
            cursor="hand2", command=self._guardar_producto
        )
        btn_guardar.pack(fill="x", pady=(35, 0))

        # ----- Tabla de productos -----
        frame_tabla = ttk.Frame(self.tab_inventario)
        frame_tabla.pack(side="left", fill="both", expand=True, padx=(0, 15), pady=15)

        columnas = ("id", "nombre", "precio", "stock")
        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("precio", text="Precio ($)")
        self.tabla.heading("stock", text="Stock")
        self.tabla.column("id", width=60, anchor="center")
        self.tabla.column("nombre", width=280, anchor="w")
        self.tabla.column("precio", width=110, anchor="e")
        self.tabla.column("stock", width=80, anchor="center")

        scroll = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scroll.set)
        self.tabla.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

    # ------------------------------------------------------------------
    # Lógica
    # ------------------------------------------------------------------
    def _cargar_productos(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for p in Product().get_all():
            self.tabla.insert(
                "", "end",
                values=(p["id"], p["name"], f"{p['price']:.2f}", p["stock"])
            )

    def _guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        precio_texto = self.entry_precio.get().strip().replace(",", ".")
        stock_texto = self.entry_stock.get().strip()

        if not nombre or not precio_texto or not stock_texto:
            messagebox.showwarning("Campos Vacíos", "Por favor completa nombre, precio y stock.")
            return

        try:
            precio = float(precio_texto)
            stock = int(stock_texto)
        except ValueError:
            messagebox.showerror("Datos inválidos", "El precio debe ser un número y el stock un entero.")
            return

        if precio < 0 or stock < 0:
            messagebox.showerror("Datos inválidos", "El precio y el stock no pueden ser negativos.")
            return

        producto = Product(name=nombre, price=precio, stock=stock)
        if producto.create():
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
            self.entry_stock.delete(0, tk.END)
            self._cargar_productos()
            self.entry_nombre.focus_set()
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto en la base de datos.")

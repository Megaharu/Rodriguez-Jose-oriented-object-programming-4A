"""inventory.py
Responsibility (SRP): manage the collection of products and locate them.
"""
from exceptions import ProductoNoEncontrado
from products import Producto


class Inventario:
    def __init__(self):
        # Dictionary code -> Producto (each with a different code and stock)
        self.productos = {
            "A100": Producto("A100", "Keyboard", 10),
            "B200": Producto("B200", "Mouse", 25),
            "C300": Producto("C300", "Monitor", 5),
            "D400": Producto("D400", "Laptop", 8),
        }

    def retirar(self, codigo, cantidad):
        """Find the product and delegate the withdrawal to Producto.retirar()."""
        # Verify that the product exists
        if codigo not in self.productos:
            raise ProductoNoEncontrado(f"Product '{codigo}' does not exist.")

        producto = self.productos[codigo]
        # No try/except here: CantidadInvalida and StockInsuficiente
        # propagate up to main.py, where they are handled.
        return producto.retirar(cantidad)
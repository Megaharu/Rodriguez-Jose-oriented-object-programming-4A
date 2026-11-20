"""products.py
Responsibility (SRP): represent a product and manage its own stock.
"""
from exceptions import CantidadInvalida, StockInsuficiente


class Producto:
    def __init__(self, codigo, nombre, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.stock = stock

    def retirar(self, cantidad):
        """Withdraw 'cantidad' units and return the remaining stock."""
        # Validation 1: must be an integer (bool is excluded because it subclasses int)
        if not isinstance(cantidad, int) or isinstance(cantidad, bool):
            # 'raise' throws the exception and stops the method right here
            raise CantidadInvalida("The quantity must be an integer.")

        # Validation 2: must be positive (zero and negatives are not valid)
        if cantidad <= 0:
            raise CantidadInvalida("The quantity must be greater than zero.")

        # Validation 3: cannot withdraw more than what is available
        if cantidad > self.stock:
            raise StockInsuficiente(
                f"Insufficient stock: requested {cantidad}, available {self.stock}."
            )

        # The stock is only modified after all validations pass,
        # so an invalid operation never alters the inventory.
        self.stock -= cantidad
        return self.stock
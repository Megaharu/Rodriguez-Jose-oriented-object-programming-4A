class ErrorInventario(Exception):
    """Base exception: all the others inherit from it, so main.py
    can catch any inventory error with a single except block."""


class ProductoNoEncontrado(ErrorInventario):
    """The product code does not exist in the inventory."""


class CantidadInvalida(ErrorInventario):
    """The quantity is zero, negative, or not an integer."""


class StockInsuficiente(ErrorInventario):
    """The requested quantity exceeds the available stock."""

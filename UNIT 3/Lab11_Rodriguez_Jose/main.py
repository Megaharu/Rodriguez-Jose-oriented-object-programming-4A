"""main.py
Responsibility (SRP): user interaction and error handling.
"""
from exceptions import ErrorInventario
from inventory import Inventario


def main():
    inventario = Inventario()

    codigo = input("Product code: ").strip()

    try:
        # int() raises ValueError if the user types text
        cantidad = int(input("Quantity to withdraw: "))
        restante = inventario.retirar(codigo, cantidad)

    except ValueError:
        # Runs when the quantity is not an integer
        print("Error: you must enter a whole number.")

    except ErrorInventario as e:
        # Catches ProductoNoEncontrado, CantidadInvalida and StockInsuficiente
        # (all of them inherit from ErrorInventario)
        print(f"Inventory error: {e}")

    else:
        # Only runs if the try block finished WITHOUT exceptions
        print("Withdrawal successful.")
        print(f"Remaining stock of {codigo}: {restante}")


if __name__ == "__main__":
    main()
class SuscripcionExpiradaError(Exception):
    """Excepción lanzada al intentar ejecutar operaciones restringidas sin una membresía activa."""
    pass

class PuntosInsuficientesError(Exception):
    """Excepción lanzada cuando una transacción excede el saldo de gemas disponible."""
    pass


class PerfilMovil:
    def __init__(self, username: str, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        if gemas < 0:
            raise ValueError("El valor inicial de las gemas no puede ser negativo.")
        self.username = username
        self.gemas = gemas
        self.racha_dias = racha_dias
        self.notificaciones_activas = notificaciones_activas

    def ganar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a ganar debe ser estrictamente positiva.")
        self.gemas += cantidad
        return self.gemas

    def gastar_gemas(self, cantidad: int) -> int:
        if cantidad <= 0:
            raise ValueError("La cantidad de gemas a gastar debe ser estrictamente positiva.")
        if cantidad > self.gemas:
            raise PuntosInsuficientesError("Saldo de gemas insuficiente para la transacción.")
        self.gemas -= cantidad
        return self.gemas


class PerfilPro(PerfilMovil):
    def __init__(self, username: str, meses_suscripcion: int, gemas: int = 50, racha_dias: int = 1, notificaciones_activas: bool = True):
        super().__init__(username, gemas, racha_dias, notificaciones_activas)
        if meses_suscripcion <= 0:
            raise ValueError("El periodo inicial de suscripción debe ser mayor a cero.")
        self.meses_suscripcion = meses_suscripcion
        self.es_pro = True

    def descargar_contenido_offline(self) -> str:
        if self.meses_suscripcion <= 0:
            self.es_pro = False
            raise SuscripcionExpiradaError("No se puede descargar contenido: la suscripción ha expirado.")
        return "Contenido descargado exitosamente"
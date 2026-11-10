import pytest
from app_movil import PerfilMovil, PerfilPro, SuscripcionExpiradaError, PuntosInsuficientesError

@pytest.fixture
def perfil_estandar():
    """Fixture para proveer una instancia estandarizada de PerfilMovil."""
    return PerfilMovil(username="usuario_test")

def test_asignacion_inicial(perfil_estandar):
    """Verificación de la asignación inicial de atributos."""
    assert perfil_estandar.username == "usuario_test"
    assert perfil_estandar.gemas == 50
    assert perfil_estandar.racha_dias == 1
    assert perfil_estandar.notificaciones_activas is True

@pytest.mark.parametrize("cantidad_ganada, gemas_esperadas", [
    (10, 60),
    (50, 100),
    (1, 51)
])
def test_ganar_gemas_valido(perfil_estandar, cantidad_ganada, gemas_esperadas):
    """Evaluación eficiente de múltiples vectores de prueba para el método ganar_gemas."""
    perfil_estandar.ganar_gemas(cantidad_ganada)
    assert perfil_estandar.gemas == gemas_esperadas

def test_ganar_gemas_invalido(perfil_estandar):
    """Validación rigurosa de propagación de error al enviar valores negativos o nulos."""
    with pytest.raises(ValueError):
        perfil_estandar.ganar_gemas(0)

def test_gastar_gemas_valido(perfil_estandar):
    """Prueba de consistencia aritmética en transacciones de saldo."""
    perfil_estandar.gastar_gemas(20)
    assert perfil_estandar.gemas == 30

def test_gastar_gemas_insuficientes(perfil_estandar):
    """Comprobación de error en estados inválidos por falta de fondos."""
    with pytest.raises(PuntosInsuficientesError):
        perfil_estandar.gastar_gemas(100)

def test_perfil_pro_isinstance():
    """Comprobación formal de la relación de herencia."""
    perfil_pro = PerfilPro(username="pro_test", meses_suscripcion=3)
    assert isinstance(perfil_pro, PerfilMovil)
    assert perfil_pro.es_pro is True

def test_perfil_pro_meses_invalidos():
    """Validación de que el periodo inicial sea mayor a cero."""
    with pytest.raises(ValueError):
        PerfilPro(username="pro_test", meses_suscripcion=0)

def test_descargar_contenido_offline_valido():
    perfil_pro = PerfilPro(username="pro_test", meses_suscripcion=1)
    resultado = perfil_pro.descargar_contenido_offline()
    assert resultado == "Contenido descargado exitosamente"

def test_descargar_contenido_offline_expirado():
    perfil_pro = PerfilPro(username="pro_test", meses_suscripcion=1)
    # Se simula el paso del tiempo donde caducan los meses
    perfil_pro.meses_suscripcion = 0 
    
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro.descargar_contenido_offline()
    
    # Se verifica el cambio de estado de la bandera booleana
    assert perfil_pro.es_pro is False
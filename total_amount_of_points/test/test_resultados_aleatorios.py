# importar el modulo de otro directorio
from src.calcularPuntos import points
import pytest


@pytest.mark.puntos_aleatorios
def test_puntos_randoms():
    assert points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']) == 10

@pytest.mark.puntos_aleatorios
def test_puntos_randoms():
    assert points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']) == 15

@pytest.mark.puntos_aleatorios
def test_puntos_randoms():
    assert points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']) == 12

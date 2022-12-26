# importar el modulo de otro directorio
from src.calcularPuntos import points
import pytest


@pytest.mark.puntos_maximos
def test_todo_ganado():
    assert points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']) == 30
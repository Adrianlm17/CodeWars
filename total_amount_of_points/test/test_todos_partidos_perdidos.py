# importar el modulo de otro directorio
from src.calcularPuntos import points
import pytest


@pytest.mark.cero_puntos
def test_todo_perdido():
    assert points(['0:1','0:2','0:3','0:4','1:2','1:3','3:4','2:3','1:2','2:3']) == 0

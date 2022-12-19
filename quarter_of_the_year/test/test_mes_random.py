# importar el modulo de otro directorio
from src.numeroTrimestre import quarter_of
import pytest


@pytest.mark.test_mes_random_1
def test_mes_random_1():
    assert quarter_of(3) == 1

@pytest.mark.test_mes_random_2
def test_mes_random_2():
    assert quarter_of(8) == 3

@pytest.mark.test_mes_random_3
def test_mes_random_3():
    assert quarter_of(11) == 4

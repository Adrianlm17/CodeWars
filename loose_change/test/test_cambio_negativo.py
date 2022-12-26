# importar el modulo de otro directorio
from src.calcularCambio import loose_change
import pytest


@pytest.mark.test_cambio_negativo
def test_cambio_negativo():
    assert loose_change((-2)) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

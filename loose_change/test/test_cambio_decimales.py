# importar el modulo de otro directorio
from src.calcularCambio import loose_change
import pytest


@pytest.mark.test_cambio_decimales
def test_cambio_decimales():
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    
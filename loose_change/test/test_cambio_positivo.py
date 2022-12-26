# importar el modulo de otro directorio
from src.calcularCambio import loose_change
import pytest


@pytest.mark.test_cambio_positivo
def test_cambio_positivo():
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}

@pytest.mark.test_cambio_positivo
def test_cambio_positivo():
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}

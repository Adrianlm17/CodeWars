# importar el modulo de otro directorio
from src.calcularCambio import loose_change
import pytest


@pytest.mark.text_cambio_cero
def text_cambio_cero():
    assert loose_change(0) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}

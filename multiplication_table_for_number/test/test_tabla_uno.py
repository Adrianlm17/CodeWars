from src.multiplication_table_for_number import multi_table
import pytest
 
 
@pytest.mark.test_tabla_uno
def test_tabla_uno():
    assert (multi_table(1)), '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10'
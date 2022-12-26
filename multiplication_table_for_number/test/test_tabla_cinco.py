from src.multiplication_table_for_number import multi_table
import pytest
 
 
@pytest.mark.test_tabla_cinco
def test_tabla_cinco():
    assert (multi_table(5)), '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50'

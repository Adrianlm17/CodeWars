from src.simple_pig_latin import pig_it
import pytest
    
    
@pytest.mark.test_thisis
def test_thisis():
    assert(pig_it('This is my string'),'hisTay siay ymay tringsay')

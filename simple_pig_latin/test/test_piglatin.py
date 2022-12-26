from src.simple_pig_latin import pig_it
import pytest
    
    
@pytest.mark.test_piglatin
def test_piglatin():
    assert(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')

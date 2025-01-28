import math
import pytest

def calcular_area_circulo(radio):
    if radio <0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * radio ** 2

def test_calcular_area_circulo():
    assert calcular_area_circulo(1) == math.pi, "El area del circulo con radio 1 no es igual a pi"
    
    assert calcular_area_circulo(0) == 0, "El area del ciruclo con radio 0 debe ser 0"
    
    with pytest.raises(ValueError):
        calcular_area_circulo(-1), "No se lanzo excepcion para un radio negativo"
        
if __name__ == "__main__":
    pytest.main([__file__])
    print("Todas las pruebas han pasado correctamente")

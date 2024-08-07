from programa import imprimir_datos_personales
from io import StringIO
import sys

def test_imprimir_datos_personales(capsys):
    nombre = "Dennis Chicaiza"
    edad = 45
    estatura = 1.64
    imprimir_datos_personales(nombre, edad, estatura)
    captured = capsys.readouterr()
    assert captured.out == "Nombre: Dennis Chicaiza\nEdad: 45\nEstatura: 1.64\n"

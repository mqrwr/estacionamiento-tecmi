import os
import tempfile
import unittest

from src.registro import registrar_ingreso, cargar


class TestRegistro(unittest.TestCase):
    def setUp(self):
        fd, self.archivo = tempfile.mkstemp(suffix=".json")
        os.close(fd)
        os.remove(self.archivo)

    def tearDown(self):
        if os.path.exists(self.archivo):
            os.remove(self.archivo)

    def test_registro_correcto(self):
        r = registrar_ingreso("abc123", "Auto", self.archivo)
        self.assertEqual(r["placa"], "ABC123")
        self.assertEqual(r["tipo"], "auto")
        self.assertEqual(len(cargar(self.archivo)), 1)

    def test_placa_duplicada(self):
        registrar_ingreso("ABC123", "auto", self.archivo)
        with self.assertRaises(ValueError):
            registrar_ingreso("abc123", "auto", self.archivo)

    def test_tipo_invalido(self):
        with self.assertRaises(ValueError):
            registrar_ingreso("XYZ789", "camion", self.archivo)

    def test_placa_vacia(self):
        with self.assertRaises(ValueError):
            registrar_ingreso("   ", "auto", self.archivo)


if __name__ == "__main__":
    unittest.main()

import unittest
from random import seed
import string

from func_generar_password import generar_password

class TestCrearPassword(unittest.TestCase):

    def setUp(self):
        seed(0)

    def test_longitud_password(self):

        longitud = 12
        password = generar_password(longitud, True, True, True, True)

        self.assertEqual(len(password), longitud)

    def test_error_sin_caracteres(self):

        with self.assertRaises(ValueError):
            generar_password(8, False, False, False, False)

    def test_caracteres_permitidos(self):

        longitud = 10
        password = generar_password(longitud, True, True, True, True)
        for char in password:
            self.assertIn(char, string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)

    def test_al_menos_un_caracter_de_cada_tipo(self):

        longitud = 8
        password = generar_password(longitud, True, True, True, True)

        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':

    unittest.main()
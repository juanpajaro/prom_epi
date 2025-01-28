#!/usr/bin/env python3
from punto_1 import calcular_imc
import unittest
import pandas as pd

class TestPromedio(unittest.TestCase):
    def test_calculo_media_imc(self):
        data_prueba = [30, 20, 10, 40, 50]
        serie_prueba = pd.Series(data=data_prueba)
        #media_imc = serie_prueba.mean()
        #print("valor_medica: {}".format(media_imc))
        testcase = serie_prueba
        expected = 30
        self.assertAlmostEqual(calcular_imc(testcase), expected, places=4)

if __name__ == '__main__':
    unittest.main()
    
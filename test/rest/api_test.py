import http.client
import os
import unittest
from urllib.request import urlopen
import time  # Añade la importación de 'time'

import pytest

BASE_URL = "http://localhost:5000"
BASE_URL_MOCK = "http://localhost:9090"
DEFAULT_TIMEOUT = [10]  # in secs

@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        global DEFAULT_TIMEOU
        url = f"{BASE_URL}/calc/add/1/2"

        start_time = time.time()
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        end_time = time.time()

        elapsed_time = end_time - start_time
        print(f"La solicitud tomó {elapsed_time} segundos")

        # Ajusta el DEFAULT_TIMEOUT basado en el tiempo de ejecución
        DEFAULT_TIMEOUT = elapsed_time + 2  # Añade un margen adicional (ajusta según sea necesario)

        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "3", "ERROR ADD"
        )

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/1/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "2", "ERROR MULTIPLY"
        )

    def test_api_divide(self):
        url = f"{BASE_URL}/calc/divide/0/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "0", "HTTP 406"
        )

    def test_api_sqrt(self):
        url = f"{BASE_URL_MOCK}/calc/sqrt/64"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
        self.assertEqual(
            response.read().decode(), "8", "ERROR SQRT"
        )

if __name__ == "__main__":  # pragma: no cover
    unittest.main()

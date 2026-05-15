import unittest
from src.tugas.MohammadRizkyAndiPutra.service import luas

class TestLuas(unittest.TestCase):

    def test_luas_positif(self):
        self.assertEqual(luas(5, 3), 15)

    def test_luas_nol(self):
        self.assertEqual(luas(0, 5), 0)

    def test_luas_negatif(self):
        self.assertEqual(luas(-2, 4), -8)

if __name__ == '__main__':
    unittest.main()
import unittest
import covicontact
import numpy as np

class TestContactMatrices(unittest.TestCase):

    def test_runs(self):

        country = {
            'POPULATION_SIZE_COUNTRY': 0,
            'P_AGE_COUNTRY': np.ones((16, 16)),
            'POPULATION_SIZE_COUNTRY': 0,
            'COUNTRY_CONTACT_MATRIX_HOUSEHOLD': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_HOUSEHOLD': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_HOUSEHOLD': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_WORK': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_ALL': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_OTHER': np.random.uniform(0, 1, size=(16, 16)),
            'COUNTRY_CONTACT_MATRIX_SCHOOL': np.random.uniform(0, 1, size=(16, 16)),
        }

        region = {
            'P_AGE_REGION':  np.ones((16, 16)),
            'POPULATION_SIZE_REGION': 0,
        }

        covicontact.mixing(country, region)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

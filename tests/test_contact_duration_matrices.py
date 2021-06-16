import unittest
import covicontact
import numpy as np

class TestContactDurationMatrices(unittest.TestCase):

    def test_runs(self):

        SECONDS_PER_MINUTE = 60

        country = {
            'MEAN_DURATION_MATRIX': np.random.uniform(0, 1, size=(16, 16)),
            'MEAN_MINUS_95_CI_MATRIX': np.random.uniform(0, 1, size=(16, 16)),
            'MEAN_HOUSEHOLD_CONTACT_MINUTES': 1,
            'STDDEV_HOUSEHOLD_CONTACT_MINUTES': 1,
            'MEAN_SCHOOL_CONTACT_MINUTES': 1,
            'STDDEV_SCHOOL_CONTACT_MINUTES': 1,
            'MEAN_WORKPLACE_CONTACT_MINUTES': 1,
            'STDDEV_WORKPLACE_CONTACT_MINUTES': 1,
            'MEAN_OTHER_CONTACT_MINUTES': 1,
            'STDDEV_OTHER_CONTACT_MINUTES': 1,
        }

        covicontact.duration(country, SECONDS_PER_MINUTE)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

import unittest
from speed_test import test_speed

class TestSpeedTest(unittest.TestCase):
    def test_speed_test_results(self):
        results = test_speed()
        self.assertIn('download', results)
        self.assertIn('upload', results)
        self.assertIn('ping', results)
        self.assertIn('server', results)
        self.assertIn('timestamp', results)

if __name__ == '__main__':
    unittest.main()

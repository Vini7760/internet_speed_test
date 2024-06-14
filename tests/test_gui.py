import unittest
from tkinter import Tk
from gui import SpeedTestApp

class TestGUI(unittest.TestCase):
    def test_gui_elements(self):
        root = Tk()
        app = SpeedTestApp(root)
        
        self.assertIsNotNone(app.label)
        self.assertIsNotNone(app.start_button)
        self.assertIsNotNone(app.results_label)

        root.destroy()

if __name__ == '__main__':
    unittest.main()

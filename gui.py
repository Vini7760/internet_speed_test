import tkinter as tk
from tkinter import ttk
from speed_test import test_speed
import utils.logger as logger

class SpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Internet Speed Test")

        self.label = ttk.Label(root, text="Click 'Start' to begin the speed test", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.start_button = ttk.Button(root, text="Start", command=self.start_test)
        self.start_button.pack(pady=20)

        self.results_label = ttk.Label(root, text="", font=("Helvetica", 12))
        self.results_label.pack(pady=20)

    def start_test(self):
        self.results_label.config(text="Testing...")
        self.root.update_idletasks()

        speed_results = test_speed()
        logger.log_speed_test_results(speed_results)

        result_text = (
            f"Download Speed: {speed_results['download']:.2f} Mbps\n"
            f"Upload Speed: {speed_results['upload']:.2f} Mbps\n"
            f"Ping: {speed_results['ping']} ms\n"
            f"Server: {speed_results['server']}\n"
            f"Timestamp: {speed_results['timestamp']}"
        )

        self.results_label.config(text=result_text)

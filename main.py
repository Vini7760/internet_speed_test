import matplotlib
matplotlib.use('Agg')
from speed_test import test_speed
import utils.logger as logger

def main():
    print("Starting speed test...")
    speed_results = test_speed()
    if speed_results:
        logger.log_speed_test_results(speed_results)
        print("Speed test completed and results logged.")
    else:
        print("Speed test failed.")

if __name__ == "__main__":
    main()

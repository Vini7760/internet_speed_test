import logging

def setup_logger():
    logger = logging.getLogger('speedtest_logger')
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('data/logs/speedtest.log')
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

logger = setup_logger()

def log_speed_test_results(results):
    logger.info(f"Download: {results['download']} Mbps, Upload: {results['upload']} Mbps, Ping: {results['ping']} ms, Server: {results['server']}, Timestamp: {results['timestamp']}")

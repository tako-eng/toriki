
import logging

def initialize_logger():
    level=logging.DEBUG
    format="[%(asctime)s %(filename)s:%(lineno)d] [%(levelname)s] --- %(message)s"
    stream_log = logging.StreamHandler()
    stream_log.setLevel(level)
    stream_log.setFormatter(logging.Formatter(format))
    logging.getLogger().setLevel(logging.DEBUG)
    logging.getLogger().addHandler(stream_log)

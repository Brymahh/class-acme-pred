import os
import sys
import logging

## set formatting for logs
logging_str = "[%(asctime)s]: %(levelname)s: %(module)s: %(message)s"

log_dir = 'logs'

log_filepath = os.path.join(log_dir, "running_log.log")
os.makedirs(log_dir, exist_ok=True)

## define logging state
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #show logs in terminal
    ]
)

# define logger object
logger=logging.getLogger("acme_logger")
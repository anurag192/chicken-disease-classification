import os
import sys
import logging

# Correct: should be a string, not a list
logging_str = '%(asctime)s - %(levelname)s - %(message)s'

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)  # Make sure the directory exists

log_file_path = os.path.join(log_dir, 'running_log.log')

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('cnnlog')

import logging
import logging.config
from pathlib import Path
import yaml

# Load the logging configuration
config_path = Path(__file__).parent.parent.parent / 'config' / 'log_config.yaml'
with open(config_path, 'r') as log_config_file:
    config = yaml.safe_load(log_config_file)
    logging.config.dictConfig(config['logging'])  # Configure the logging system

 # create logger objects 
internal_error_logger = logging.getLogger('internal_errors')
registration_error_logger = logging.getLogger('registration_error')
page_errors_logger = logging.getLogger('page_errors')

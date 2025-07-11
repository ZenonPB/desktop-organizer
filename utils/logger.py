import logging
import os
from datetime import datetime
from config.settings import Settings

def setup_logger():
    logger = logging.getLogger("DesktopOrganizer")
    logger.setLevel(getattr(logging, Settings.LOG_LEVEL))

    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        '%%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    if Settings.LOG_TO_FILE:
        log_directory = Settings.get_log_directory()
        os.makedirs(log_directory, exist_ok=True)

        log_file = os.path.join
        (log_directory, 
         f"organizer_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    if Settings.LOG_TO_CONSOLE:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger
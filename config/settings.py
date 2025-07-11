import os
from core.organizer import DesktopOrganizer

class Settings:
    
    VERSION = "0.1"

    DESKTOP_PATH = str(os.path.join(os.path.expanduser("~"), "Desktop"))
    ROOT_FOLDER_NAME = DesktopOrganizer.organized_root

    LOG_LEVEL = "INFO"
    LOG_TO_FILE = True
    LOG_TO_CONSOLE = True

    MAX_FILE_SIZE_MB = 1000  # Maximum file size to process in MB
    BACKUP_ENABLED = False

    OVERWRITE_EXISTING_FILES = False
    ORGANIZE_HIDDEN_FILES = False

    @classmethod
    def get_log_directory(cls):
        return os.path.join(cls.DESKTOP_PATH, "organizer_logs")
    
import os
import shutil
import logging
from datetime import datetime
from utils.helpers import create_backup, clean_old_backups
from config.config_manager import ConfigManager

logger = logging.getLogger(__name__)

def move_file(src_path: str, dest_root: str, category: str):
    try:
        filename = os.path.basename(src_path)
        dest_dir = os.path.join(dest_root, category)
        dest_path = os.path.join(dest_dir, filename)

        # Verifies if needs to create a backup
        config = ConfigManager.load_config()
        if config.get('enable_backup', False):
            backup_dir = os.path.join(os.path.dirname(src_path), 'backups')
            create_backup(src_path, backup_dir)
            clean_old_backups(backup_dir, config.get('max_backups', 7))

        # If the destination file already exists, create a unique filename
        os.makedirs(dest_dir, exist_ok=True)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base}_{timestamp}{ext}"
            dest_path = os.path.join(dest_dir, new_filename)

        shutil.move(src_path, dest_path)
        logger.info(f"Moved file {src_path} to {dest_path}")
        return True
    
    except Exception as e:
        logger.error(f"Error moving file {src_path} to {dest_root}/{category}: {e}")
        return False

def _get_unique_filename(src_path: str) -> str:
    directory = os.path.dirname(src_path)
    filename = os.path.basename(src_path)
    name, ext = os.path.splitext(filename)

    counter = 1
    while True:
        new_filename = f"{name} ({counter}){ext}"
        new_src_path = os.path.join(directory, new_filename)
        if not os.path.exists(new_src_path):
            return new_src_path
        counter += 1
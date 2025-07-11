import os
import shutil
import logging
import datetime

logger = logging.getLogger(__name__)

def move_file(file_path: str, dest_root: str, category: str):
    try:
        filename = os.path.basename(file_path)
        dest_dir = os.path.join(dest_root, category)
        dest_path = os.path.join(dest_dir, filename)

        os.makedirs(dest_dir, exist_ok=True)
        if os.path.exists(dest_path):
            base, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            new_filename = f"{base}_{timestamp}{ext}"
            dest_path = os.path.join(dest_dir, new_filename)

        shutil.move(file_path, dest_path)

        logger.info(f"Moved file {file_path} to {dest_path}")
        return True
    except Exception as e:
        logger.error(f"Error moving file {file_path} to {dest_root}/{category}: {e}")
        return False

def _get_unique_filename(file_path: str) -> str:
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)

    counter = 1
    while True:
        new_filename = f"{name} ({counter}){ext}"
        new_file_path = os.path.join(directory, new_filename)
        if not os.path.exists(new_file_path):
            return new_file_path
        counter += 1
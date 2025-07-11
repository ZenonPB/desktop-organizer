import os
import shutil

def get_file_size_mb(file_path):
    try:
        size_bytes = os.path.getsize(file_path)
        return size_bytes / (1024 * 1024)  # Convert bytes to MB
    except OSError as e:
        print(f"Error getting size for {file_path}: {e}")
        return None
    
def is_too_large(file_path, max_size_mb=1000):
    return get_file_size_mb(file_path) > max_size_mb if get_file_size_mb(file_path) is not None else False

def create_backup(file_path, backup_dir):
    try:
        os.makedirs(backup_dir, exist_ok=True)
        filename = os.path.basename(file_path)
        backup_path = os.path.join(backup_dir, filename)
        shutil.copy2(file_path, backup_path)
        print(f"Backup created for {file_path} at {backup_path}")

    except Exception as e:
        print(f"Error creating backup for {file_path}: {e}")
        return False
    
    return True

def save_filename(filename):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip() 

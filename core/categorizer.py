import os 
from config import file_categorizer

def categorize_file(file_path):
    try:

        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_name)[1].lower()

        for category, extensions in file_categorizer.CATEGORY_MAPPING.items():
            if extension in extensions:
                return category
            
        return "Others"
    except Exception as e:
        print(f"Error categorizing file {file_path}: {e}")
        return "Error"


import os
import shutil

# Choose the folder you want to organize
folder_path = input("Enter the folder path to organize (example: /Users/yourname/Downloads): ").strip()

if not os.path.isdir(folder_path):
    print("Invalid folder path.")
    raise SystemExit

# File type categories
CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff", ".heic"],
    "Videos": [".mp4", ".mov", ".mkv", ".avi", ".wmv", ".flv", ".webm"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

def get_category(file_extension: str) -> str:
    ext = file_extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"

# Create folders if they don't exist
for category in list(CATEGORIES.keys()) + ["Others"]:
    os.makedirs(os.path.join(folder_path, category), exist_ok=True)

moved = 0

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(filename)
    category = get_category(ext)

    destination_folder = os.path.join(folder_path, category)
    destination_path = os.path.join(destination_folder, filename)

    # Avoid overwriting files with the same name
    if os.path.exists(destination_path):
        base, extension = os.path.splitext(filename)
        counter = 1
        while os.path.exists(destination_path):
            new_name = f"{base}_{counter}{extension}"
            destination_path = os.path.join(destination_folder, new_name)
            counter += 1

    shutil.move(file_path, destination_path)
    moved += 1

print(f"Done! Moved {moved} files into organized folders.")

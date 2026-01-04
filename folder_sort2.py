import os
import shutil

# 1. Use double backslashes or a raw string for Windows paths
downloads = r"C:\Users\VINOD\Downloads"

for file in os.listdir(downloads):
    path = os.path.join(downloads, file)
    
    # 2. Only process files, not folders
    if os.path.isfile(path):
        # 3. Get the extension (e.g., 'jpg' or 'txt')
        parts = file.split('.')
        
        # Check if the file actually has an extension
        if len(parts) > 1:
            ext = parts[-1].lower() # .lower() helps keep folders uniform
            folder = os.path.join(downloads, ext)
            
            # 4. Create folder if it doesn't exist (True must be capitalized)
            os.makedirs(folder, exist_ok=True)
            
            # 5. Move the file
            try:
                shutil.move(path, folder)
                print(f"Moved: {file} -> {ext}/")
            except Exception as e:
                print(f"Could not move {file}: {e}")
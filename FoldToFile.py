import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import mysql.connector

# Update these with your actual MySQL details
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'database': 'YOUR_DATABASE_NAME'
}

def log_to_database(file_name, ext, src, dest):
    """Handles the MySQL INSERT operation."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = "INSERT INTO file_move_history (file_name, extension, source_path, destination_path) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (file_name, ext, src, dest))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

def start_organizing():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return

    all_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    total = len(all_files)
    
    if total == 0:
        messagebox.showinfo("Info", "No files to move.")
        return

    for i, file in enumerate(all_files):
        # Logic to move file
        ext = file.split('.')[-1].lower() if '.' in file else 'others'
        dest_folder = os.path.join(folder_path, ext)
        os.makedirs(dest_folder, exist_ok=True)
        
        src_path = os.path.join(folder_path, file)
        dest_path = os.path.join(dest_folder, file)
        
        shutil.move(src_path, dest_path)
        log_to_database(file, ext, src_path, dest_path)

        # Update Visuals
        progress['value'] = ((i + 1) / total) * 100
        status_var.set(f"Moving: {file}")
        root.update_idletasks()

    messagebox.showinfo("Success", f"Done! {total} files organized and logged.")
    status_var.set("Ready")

# GUI Initialization
root = tk.Tk()
root.title("File Organizer & MySQL Logger")
root.geometry("400x200")

status_var = tk.StringVar(value="Ready")
tk.Label(root, textvariable=status_var).pack(pady=10)

progress = ttk.Progressbar(root, length=300, mode='determinate')
progress.pack(pady=10)

tk.Button(root, text="Select Folder", command=start_organizing).pack(pady=20)

root.mainloop()
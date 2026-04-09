import os
import shutil
from datetime import datetime

# User Configuration
student_id = "2025-4754"  
student_name = "John Richmond M. Cleofe" 
target_file = "Act5_document.txt" 

# Paths
source_dir = "Documents/Activity_5_Exercises/"
backup_dir = os.path.join(source_dir, f"backup_{student_id}")
log_file_path = os.path.join(backup_dir, f"backup_log_{student_id}.txt")

def run_smart_backup(filename):
    # 1. Ensure the source and backup directories exist
    source_path = os.path.join(source_dir, filename)
    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' not found.")
        return

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # 2. Generate Timestamp and Unique Filename
    # Format: YYYYMMDD_HHMMSS
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    name_part, ext_part = os.path.splitext(filename)
    backup_filename = f"{name_part}_{student_id}_{timestamp}{ext_part}"
    destination_path = os.path.join(backup_dir, backup_filename)

    # 3. Copy the file
    shutil.copy2(source_path, destination_path)
    file_size = os.path.getsize(destination_path)

    # 4. Update the Log File
    log_entry = (
        f"--- Backup Entry ---\n"
        f"Student ID: {student_id}\n"
        f"Student Name: {student_name}\n"
        f"Original Filename: {filename}\n"
        f"Timestamp: {timestamp}\n"
        f"File Size: {file_size} bytes\n"
        f"Backup Path: {destination_path}\n\n"
    )

    with open(log_file_path, "a") as log:
        log.write(log_entry)

    # 5. Output Confirmation
    print(f"Backup completed for {student_id} ({student_name})")
    print(f"File saved as: {backup_filename}")
    print(f"Log updated at: {log_file_path}")

if __name__ == "__main__":
    run_smart_backup(target_file)
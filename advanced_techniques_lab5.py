# ============================================
# ADVANCED TECHNIQUES - ONE CELL VERSION
# ============================================

# ================================
# 1. TRY-EXCEPT FOR ERROR HANDLING
# ================================

try:
    with open("nonexistent.txt", "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("[1] Error: File does not exist.")


# ============================================
# 2. TIMESTAMPED BACKUP FUNCTION
# ============================================

from datetime import datetime
import shutil
from pathlib import Path

def create_backup(original_path):
    original_path = Path(original_path)

    if original_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{original_path.stem}_backup_{timestamp}{original_path.suffix}"
        backup_path = original_path.parent / backup_name

        shutil.copy(original_path, backup_path)
        print(f"[2] Backup created: {backup_path}")
    else:
        print("[2] No original file found to back up.")


# Test backup function
test_file = Path.home() / "Documents" / "Surname_Activity_5" / "test.txt"
test_file.parent.mkdir(parents=True, exist_ok=True)
test_file.write_text("Sample content for backup test.")

create_backup(test_file)


# ============================================
# 3. HANDLING USER INPUT ERRORS
# ============================================

filename = "sample"  # replace with input() if needed

# Simulate validation
filename = filename.strip()
if not filename.endswith(".txt"):
    print("[3] Warning: Filename should end with '.txt'. Appending extension.")
    filename += ".txt"

print(f"[3] Final filename: {filename}")


# ============================================
# 4. DETECT FILE TYPE AND SIZE
# ============================================

file_path = Path.home() / "Documents" / "Surname_Activity_5" / filename

# Ensure file exists
file_path.write_text("This is a sample text file for size checking.")

if file_path.suffix == ".txt" and file_path.stat().st_size < 100000:
    with open(file_path, "r", encoding="utf-8") as f:
        print("[4] File content:\n", f.read())
else:
    print("[4] File is either too large or not a .txt file.")


# ============================================
# 5. LOGGING FILE OPERATIONS
# ============================================

def log_action(action, filename):
    log_file = Path.home() / "Documents" / "Surname_Activity_5" / "file_log.txt"

    with open(log_file, "a", encoding="utf-8") as log:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {action} - {filename}\n")

    print(f"[5] Logged action: {action} - {filename}")


# Test logging
log_action("CREATE", "test.txt")
log_action("BACKUP", "test_backup.txt")
log_action("READ", filename)
# ============================================
# ACTIVITY 5: FILE HANDLING (ONE-CELL VERSION)
# ============================================

# =========================
# 1. WRITING TO A FILE
# =========================

# Step 1: Import Path from pathlib
from pathlib import Path

# Step 2: Define a custom folder in your Documents directory
# (Try It Applied: Changed folder name to Surname_Activity_5)
output_dir = Path.home() / "Documents" / "Surname_Activity_5"
output_dir.mkdir(exist_ok=True)  # Creates folder if missing

# Step 3: Define the file path
file_path = output_dir / "Act5_example.txt"

# Step 4: Write text to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    # (Try It Applied: Added third line)
    file.write("Python makes file handling easy!\n")

# Step 5: Confirm that the file is saved
print(f"File saved to: {file_path.resolve()}")


# =========================
# 2. READING FROM A FILE
# =========================

# Step 1: Read the entire file content if it exists
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    print("\nFile content:\n", content)

# Step 2: Read line-by-line
with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        print(f"Line {line_number}: {line.strip()}")

# (Try It Applied: Print only lines with "Python" + word count)
print("\nFiltered lines containing 'Python' and word count:")
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        if "Python" in line:
            words = line.split()
            print(f"{line.strip()} | Word count: {len(words)}")


# =========================
# 3. APPENDING DATA
# =========================

# Step 1: Open file in append mode
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")

# Step 2: Confirm that data was added
print("\nData appended successfully.")

# (Try It Applied: Append multiple lines + user input)
lines_to_add = ["Line A", "Line B", "Line C"]
with open(file_path, "a", encoding="utf-8") as file:
    file.writelines("\n" + line for line in lines_to_add)

user_input = input("\nEnter a line to append: ")
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + user_input)


# =========================
# 4. SAFE FILE OPERATIONS WITH BACKUP
# =========================

# Step 1: Import additional libraries
from datetime import datetime
import shutil

# Step 2: Define working directory
backup_dir = Path.home() / "Documents" / "Surname_Activity_5"
backup_dir.mkdir(exist_ok=True)

# Step 3: Define a function to write a file with backup
def write_with_backup(filename: str, content: str):
    file_path = backup_dir / filename

    # Create backup if file exists
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # (Try It Applied: Added surname in backup filename)
        backup_path = file_path.with_name(
            f"{file_path.stem}_Surname_backup_{timestamp}{file_path.suffix}"
        )
        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")

    # Write the new content
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)
        print(f"File saved: {file_path.name}")

# Step 4: Define a function to read the file content
def read_file(filename: str):
    file_path = backup_dir / filename
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Step 5: Run demonstration
print("\n=== File Operations Demo ===")

print("\n1. Creating new file:")
write_with_backup("demo.txt", "Initial content")

print("\n2. Updating file (with backup):")
write_with_backup("demo.txt", "Updated content")

print("\n3. Reading file:")
print(read_file("demo.txt"))

print("\n4. Listing backups:")
for backup in backup_dir.glob("*backup*"):
    print("-", backup.name)


# =========================
# 5. MENU-DRIVEN FILE MANAGER
# =========================

def file_manager():
    file_name = input("\nEnter filename (e.g., notes.txt): ")
    file_path = backup_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. Exit")
        # (Try It Applied: Added option 6)
        print("6. List backup files")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            content = input("Enter content to write:\n")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("File written successfully.")

        elif choice == "2":
            more = input("Enter content to append:\n")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Content appended.")

        elif choice == "3":
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4":
            if file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = file_path.with_name(
                    f"{file_path.stem}_Surname_backup_{timestamp}{file_path.suffix}"
                )
                shutil.copy2(file_path, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        elif choice == "5":
            print("Exiting the file manager.")
            break

        elif choice == "6":
            print("\nBackup files:")
            backups = list(backup_dir.glob("*backup*"))
            if backups:
                for b in backups:
                    print("-", b.name)
            else:
                print("No backups found.")

        else:
            print("Invalid choice. Please try again.")


# Step 4: Run the menu-driven tool
if __name__ == "__main__":
    file_manager()
# ============================================
# DATA AND OBSERVATION (ONE CELL VERSION)
# ============================================

from pathlib import Path
import shutil
import json
import csv
import os
import time

# Personal details
student_id = "2025-4754"
student_name = "John Richmond M. Cleofe"

# Base directory (Try It applied: Surname_Activity_5)
documents_path = Path.home() / "Documents" / "Cleofe_Activity_5"
documents_path.mkdir(parents=True, exist_ok=True)


# =====================================================
# 1. CREATE AND WRITE TO A FILE
# =====================================================
# Expected Output:
# A new file is created with initial content.

file_path = documents_path / f"intro_{student_id}.txt"
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!")

print(f"[1] File created at: {file_path}")

# Actual Output:
# File created at path

# Observation:
# File is successfully created and text is written.


# =====================================================
# 2. READ FILE CONTENT
# =====================================================
# Expected Output:
# The content of an existing file is displayed.

content = file_path.read_text()
print("\n[2] File Content:\n", content)

# Observation:
# The file content is correctly read and displayed.


# =====================================================
# 3. APPEND TO A FILE
# =====================================================
# Expected Output:
# A new line is added to the existing file.

with file_path.open("a") as f:
    f.write("\nThis is a new line.")

# (Try It Applied: user input append)
user_line = "Additional user line"  # replace input() if needed
with file_path.open("a") as f:
    f.write("\n" + user_line)

print(f"[3] Line appended to: {file_path}")

# Observation:
# File content increases after appending.


# =====================================================
# 4. WRITE MULTIPLE LINES
# =====================================================
# Expected Output:
# Multiple lines are written into a new file.

lines_file = documents_path / f"lines_{student_id}.txt"
lines = ["Line 1", "Line 2", "Line 3"]

# (Try It Applied: more lines)
lines.extend(["Line 4", "Line 5"])

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print(f"[4] Multiple lines written to: {lines_file}")

# Observation:
# Multiple lines stored correctly.


# =====================================================
# 5. READ FILE LINE BY LINE
# =====================================================
# Expected Output:
# Each line from the file is displayed one by one.

print("\n[5] Reading line by line:")
with lines_file.open("r") as f:
    for line in f:
        print(line.strip())

# Observation:
# Lines are processed individually.


# =====================================================
# 6. COUNT WORDS IN FILE
# =====================================================
# Expected Output:
# The total word count in a file is displayed.

text = lines_file.read_text()
word_count = len(text.split())

print(f"\n[6] {student_name} (ID: {student_id}) - Word count: {word_count}")

# Observation:
# Word count is calculated using split().


# =====================================================
# 7. COPY FILE
# =====================================================
# Expected Output:
# A file is copied to a new location.

src = file_path
dst = documents_path / f"intro_copy_{student_id}.txt"

shutil.copy(src, dst)
print(f"\n[7] File copied from {src.name} to {dst.name}")

# Observation:
# File duplication successful.


# =====================================================
# 8. RENAME FILE
# =====================================================
# Expected Output:
# A file is renamed.

old_file = dst
new_file = documents_path / f"intro_renamed_{student_id}.txt"

old_file.rename(new_file)
print(f"[8] File renamed to: {new_file.name}")

# Observation:
# File name updated successfully.


# =====================================================
# 9. DELETE FILE
# =====================================================
# Expected Output:
# An existing file is deleted.

if new_file.exists():
    new_file.unlink()
    print(f"[9] File deleted: {new_file}")
else:
    print("[9] File not found.")

# Observation:
# File removed from directory.


# =====================================================
# 10. CREATE DIRECTORY
# =====================================================
# Expected Output:
# A new subdirectory is created.

new_dir = documents_path / f"data_{student_id}"
new_dir.mkdir(parents=True, exist_ok=True)

print(f"[10] Directory created: {new_dir}")

# Observation:
# Folder structure created successfully.


# =====================================================
# 11. WRITE JSON FILE
# =====================================================
# Expected Output:
# A JSON file is created containing structured data.

data = {"name": student_name, "age": 21, "course": "Python Programming"}
json_file = new_dir / f"student_{student_id}.json"

with json_file.open("w") as f:
    json.dump(data, f, indent=4)

print(f"[11] JSON written at: {json_file}")

# Observation:
# Data stored in JSON format.


# =====================================================
# 12. READ JSON FILE
# =====================================================
# Expected Output:
# JSON data is read and displayed.

with json_file.open("r") as f:
    data_loaded = json.load(f)

print("\n[12] JSON Content:", data_loaded)

# Observation:
# JSON file read successfully.


# =====================================================
# 13. WRITE CSV FILE
# =====================================================
# Expected Output:
# A CSV file is created with structured rows.

csv_file = documents_path / f"students_{student_id}.csv"

rows = [
    ["Name", "Student ID", "Score"],
    ["Anna", "2025-1001", 90],
    ["Ben", "2025-1002", 85],
    [student_name, student_id, 95]
]

with csv_file.open("w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print(f"[13] CSV created at: {csv_file}")

# Observation:
# CSV file successfully written.


# =====================================================
# 14. READ CSV FILE
# =====================================================
# Expected Output:
# CSV content displayed row by row.

print("\n[14] CSV Content:")
with csv_file.open("r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Observation:
# CSV read correctly.


# =====================================================
# 15. FILE NOT FOUND HANDLING
# =====================================================
# Expected Output:
# Error message when file does not exist.

missing_file = documents_path / f"missing_{student_id}.txt"

try:
    print(missing_file.read_text())
except FileNotFoundError:
    print(f"[15] File not found for Student ID: {student_id}")

# Observation:
# Exception handling works properly.


# =====================================================
# 16. COUNT .TXT FILES
# =====================================================
# Expected Output:
# Number of .txt files displayed.

txt_files = list(documents_path.glob("*.txt"))

print(f"\n[16] Found {len(txt_files)} .txt files:")
for f in txt_files:
    print("-", f.name)

# Observation:
# File filtering using glob works.


# =====================================================
# 17. FILE METADATA
# =====================================================
# Expected Output:
# File size and modification date displayed.

if file_path.exists():
    stat = file_path.stat()
    print(f"\n[17] File: {file_path.name}")
    print(f"Size: {stat.st_size} bytes")
    print(f"Last Modified: {time.ctime(stat.st_mtime)}")

# Observation:
# Metadata accessed successfully.


# =====================================================
# 18. UPPERCASE AND NUMBER LINES
# =====================================================
# Expected Output:
# Lines rewritten in uppercase and numbered.

lines = lines_file.read_text().splitlines()

with lines_file.open("w") as f:
    for i, line in enumerate(lines, 1):
        f.write(f"{i}: {line.upper()}\n")

print(f"\n[18] Lines formatted.")

# Observation:
# Text transformation successful.


# =====================================================
# 19. REVERSE FILE CONTENT
# =====================================================
# Expected Output:
# Lines reversed.

lines = lines_file.read_text().splitlines()
lines.reverse()

with lines_file.open("w") as f:
    f.write("\n".join(lines))

print("[19] Lines reversed.")

# Observation:
# Order of lines changed.


# =====================================================
# 20. MERGE TWO FILES
# =====================================================
# Expected Output:
# Two files merged into one.

merged = documents_path / f"merged_{student_id}.txt"

with merged.open("w") as mf:
    mf.write(file_path.read_text())
    mf.write("\n")
    mf.write(lines_file.read_text())

print(f"[20] Files merged into: {merged}")

# Observation:
# Contents successfully combined.
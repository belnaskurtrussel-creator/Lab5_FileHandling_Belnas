print("1.)")

# Create and Write to a File 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
student_name = "Kurt Russel S. Belnas" 
 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
documents_path.mkdir(parents=True, exist_ok=True) 
 
file_path = documents_path / f"intro_{student_id}.txt" 
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!") 
 
print(f"File created and text written at: {file_path}")



print("2.)")

# Read File Content 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
 
documents_path = Path.home() / "Documents" / "Activity_5_Files"  
file_path = documents_path / f"intro_{student_id}.txt" 
 
content = file_path.read_text() 
print(content) 



print("3.)")

# Append to a File 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"intro_{student_id}.txt" 
 
with file_path.open("a") as f: 
    f.write("\nThis is a new line.") 
print(f"Line appended to: {file_path}") 



print("4.)")

# Write Multiple Lines 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
file_path = documents_path / f"lines_{student_id}.txt" 
 
lines = ["Line 1", "Line 2", "Line 3"] 
with file_path.open("w") as f: 
    f.write("\n".join(lines)) 
print(f"Multiple lines written to: {file_path}") 



print("5.)")

# Read File Line by Line 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
with file_path.open("r") as f: 
    for line in f: 
        print(line.strip()) 



print("6.)")

# Count Words in File 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
student_name = "Kurt Russel S. Belnas" 
 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
text = file_path.read_text() 
word_count = len(text.split()) 
 
print(f"{student_name} (ID: {student_id}) - Word count in file '{file_path.name}': {word_count}") 



print("7.)")

# Cell 1: Create and Write to a File from pathlib import Path 
 
student_id = "TUPM-25-0291"
student_name = "Kurt Russel S. Belnas" 
 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
documents_path.mkdir(parents=True, exist_ok=True)
 
file_path = documents_path / f"intro_{student_id}.txt" 
file_path.write_text(f"Welcome {student_name} (ID: {student_id}) to File Handling in Python!") 
 
print(f"File created and text written at: {file_path}") 
 
# Cell 2: Copy File 
import shutil 
from pathlib import Path 
 
student_id = "TUPM-25-0291"
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
 
# Define source and destination 
src = documents_path / f"intro_{student_id}.txt" 
dst = documents_path / f"intro_copy_{student_id}.txt" 
 
# Copy file 
shutil.copy(src, dst) 
print(f"File copied successfully from {src.name} to {dst.name}.") 



print("8.)")

# Rename File 
from pathlib import Path 
 
# Personal details (keep consistent per activity) 
student_id = "TUPM-25-0291"
 
# Define directory path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
 
# Define old and new file paths 
old_file = documents_path / f"intro_copy_{student_id}.txt" 
new_file = documents_path / f"intro_renamed_{student_id}.txt" 

# Rename file 
old_file.rename(new_file) 
print(f"File renamed successfully from {old_file.name} to {new_file.name}.") 



print("9.)")

# Delete File 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define file path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
file_path = documents_path / f"intro_renamed_{student_id}.txt" 
 
# Check and delete file if it exists 
if file_path.exists(): 
    file_path.unlink() 
    print(f"File deleted successfully from: {file_path}") 
else: 
    print(f"No file found to delete at: {file_path}") 



print("10.)")

# Create Directory 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define base and new directory paths 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
new_dir = documents_path / f"data_{student_id}" 
 
# Create the new directory 
new_dir.mkdir(parents=True, exist_ok=True) 
 
print(f"Subdirectory created at: {new_dir}") 



print("11.)")

# Write JSON File 
import json 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define directory and file path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
data_dir = documents_path / f"data_{student_id}" 
data_dir.mkdir(parents=True, exist_ok=True) 
 
# Sample data 
data = {"name": "Your Name", "age": 21, "course": 
"Python Programming"} 
 
# Write JSON file 
file_path = data_dir / f"student_{student_id}.json" 
with file_path.open("w") as f: 
    json.dump(data, f, indent=4) 
 
print(f"JSON file written at: {file_path}") 



print("12.)")

# Read JSON File 
import json 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define the path to the JSON file 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"data_{student_id}" / f"student_{student_id}.json" 
 
# Read and display JSON content 
with file_path.open("r") as f: 
    data = json.load(f) 
 
print(data) 



print("13.)")

# Write CSV File 
import csv 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
student_name = "Kurt Russel S. Belnas" 
 
# Define directory and file path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
file_path = documents_path / f"students_{student_id}.csv" 

# Sample data to write 
rows = [ 
    ["Name", "Student ID", "Score"], 
    ["Anna", "2025-1001", 90], 
    ["Ben", "2025-1002", 85], 
    [student_name, student_id, 95]   
] 
 
# Write CSV file 
with file_path.open("w", newline='') as f: 
    writer = csv.writer(f) 
    writer.writerows(rows) 
 
print(f"CSV file created at: {file_path}") 



print("14.)")

# Read CSV File 
import csv 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define the file path 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"students_{student_id}.csv" 
 
# Read and display CSV content 
with file_path.open("r") as f: 
    reader = csv.reader(f) 
    for row in reader: 
        print(row) 



print("15.)")

# File Not Found Handling 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define a path to a file that does not exist 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"missing_file_{student_id}.txt" 
 
# Attempt to read the file and handle error 
try: 
    print(file_path.read_text()) 
except FileNotFoundError: 
    print(f"File not found for Student ID: {student_id}") 



print("16.)")

# Count .txt Files 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define directory path 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
 
# Find all .txt files in the directory 
txt_files = list(documents_path.glob("*.txt")) 
 
# Display count and file names 
print(f"Student ID: {student_id}") 
print(f"Found {len(txt_files)} .txt files in {documents_path}") 
for file in txt_files: 
    print(file.name)



print("17.)")

# File Metadata 
import os 
import time 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define file path 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"intro_{student_id}.txt" 
 
# Retrieve and display file metadata 
if file_path.exists(): 
    stat = file_path.stat() 
    print(f"Student ID: {student_id}") 
    print(f"File: {file_path.name}") 
    print(f"Size: {stat.st_size} bytes") 
    print(f"Last Modified: {time.ctime(stat.st_mtime)}") 
else: 
    print(f"File {file_path.name} not found for Student ID: {student_id}") 



print("18.)")
# Uppercase and Number Lines 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define file path 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
# Ensure file exists before reading 
if not file_path.exists(): 
    sample_lines = ["Line 1", "Line 2", "Line 3"] 
    file_path.write_text("\n".join(sample_lines)) 
    print(f"Sample file created for Student ID: {student_id}") 
 
# Read, process, and rewrite the file with numbered uppercase lines 
lines = file_path.read_text().splitlines() 
with file_path.open("w") as f: 
    for i, line in enumerate(lines, 1): 
        f.write(f"{i}: {line.upper()}\n") 
 
print(f"Lines formatted and updated in file: {file_path}") 



print("19.)")

# Reverse File Content 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define file path 
file_path = Path.home() / "Documents" / "Activity_5_Files" / f"lines_{student_id}.txt" 
 
# Ensure file exists before processing 
if not file_path.exists(): 
    sample_lines = ["Line 1", "Line 2", "Line 3"] 
    file_path.write_text("\n".join(sample_lines)) 
    print(f"Sample file created for Student ID: {student_id}") 
 
# Read, reverse, and overwrite the file 
lines = file_path.read_text().splitlines() 
lines.reverse() 

with file_path.open("w") as f: 
    f.write("\n".join(lines)) 
 
print(f"File lines reversed for Student ID: {student_id}") 



print("20.)")

# Merge Two Files 
from pathlib import Path 
 
# Personal details 
student_id = "TUPM-25-0291"
 
# Define file paths 
documents_path = Path.home() / "Documents" / "Activity_5_Files" 
f1 = documents_path / f"intro_{student_id}.txt" 
f2 = documents_path / f"lines_{student_id}.txt" 
merged = documents_path / f"merged_{student_id}.txt" 
 
# Ensure both source files exist 
if not f1.exists(): 
    f1.write_text(f"Welcome {student_id} to File Handling in Python!") 
    print(f"Sample intro file created for Student ID: {student_id}") 
 
if not f2.exists(): 
    f2.write_text("Line 1\nLine 2\nLine 3") 
    print(f"Sample lines file created for Student ID: {student_id}") 
 
# Merge contents of both files 
with merged.open("w") as mf: 
    mf.write(f1.read_text()) 
    mf.write("\n") 
    mf.write(f2.read_text()) 
 
print(f"Files merged successfully for Student ID: {student_id}") 
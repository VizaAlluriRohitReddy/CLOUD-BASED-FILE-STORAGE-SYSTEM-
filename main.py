# main.py
# -------------------------------
# Cloud-Based File Storage System (Simple Python Project)
# Developed by: Viza Alluri Rohit Reddy
# Internship: Valise Technologies | Team 10
# -------------------------------

import os
import shutil
import uuid
import csv
from datetime import datetime

# === Directories and file paths ===
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_DIR = os.path.join(PROJECT_DIR, "storage")
DB_PATH = os.path.join(PROJECT_DIR, "file_database.csv")


# === Step 1: Ensure folders and database file exist ===
def ensure_setup():
    os.makedirs(STORAGE_DIR, exist_ok=True)
    if not os.path.exists(DB_PATH):
        with open(DB_PATH, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["key", "original_filename", "stored_filename", "upload_timestamp"])


# === Step 2: Generate a unique key for each uploaded file ===
def generate_key():
    return uuid.uuid4().hex[:8]  # first 8 chars of UUID


# === Step 3: Upload a file ===
def upload_file(source_path):
    if not os.path.isfile(source_path):
        return False, "❌ Source file does not exist!"

    original_name = os.path.basename(source_path)
    key = generate_key()
    stored_name = f"{key}_{original_name}"
    dest_path = os.path.join(STORAGE_DIR, stored_name)

    try:
        shutil.copy2(source_path, dest_path)
    except Exception as e:
        return False, f"❌ Failed to copy file: {e}"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    # Record in CSV "database"
    with open(DB_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([key, original_name, stored_name, timestamp])

    return True, f"✅ File uploaded successfully! Unique Key: {key}"


# === Step 4: Retrieve file info by key ===
def get_file_info_by_key(key):
    with open(DB_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["key"] == key:
                return row
    return None


# === Step 5: Download a file by key ===
def download_file(key, target_dir):
    info = get_file_info_by_key(key)
    if not info:
        return False, "❌ Invalid key!"

    stored_name = info["stored_filename"]
    src = os.path.join(STORAGE_DIR, stored_name)
    if not os.path.isfile(src):
        return False, "⚠️ File missing in storage."

    os.makedirs(target_dir, exist_ok=True)
    dest = os.path.join(target_dir, info["original_filename"])
    try:
        shutil.copy2(src, dest)
    except Exception as e:
        return False, f"❌ Download failed: {e}"

    return True, f"✅ File downloaded successfully to: {dest}"


# === Step 6: List all uploaded files ===
def list_all_files():
    rows = []
    with open(DB_PATH, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


# === Step 7: Command-line interface ===
def cli():
    ensure_setup()
    print("\n==============================")
    print("📦 Simple Cloud File Storage System (Python Only)")
    print("==============================")
    print("Commands: upload | download | list | info | exit")

    while True:
        cmd = input("\n>> ").strip().lower()

        if cmd == "exit":
            print("👋 Exiting... Bye!")
            break

        elif cmd == "upload":
            source_path = input("Enter the full path of file to upload: ").strip()
            ok, msg = upload_file(source_path)
            print(msg)

        elif cmd == "download":
            key = input("Enter file key to download: ").strip()
            target_dir = input("Enter folder path to save (default: ./downloads): ").strip() or "./downloads"
            ok, msg = download_file(key, target_dir)
            print(msg)

        elif cmd == "list":
            rows = list_all_files()
            if not rows:
                print("No files uploaded yet.")
            else:
                print("\nKey | Original Filename | Stored Filename | Uploaded At")
                print("-------------------------------------------------------------")
                for r in rows:
                    print(f"{r['key']} | {r['original_filename']} | {r['stored_filename']} | {r['upload_timestamp']}")

        elif cmd == "info":
            key = input("Enter key to view file info: ").strip()
            info = get_file_info_by_key(key)
            if info:
                print("\nFile Information:")
                for k, v in info.items():
                    print(f"{k}: {v}")
            else:
                print("❌ No file found with that key.")

        else:
            print("⚠️ Invalid command! Try: upload | download | list | info | exit")


# === Run the program ===
if __name__ == "__main__":
    cli()
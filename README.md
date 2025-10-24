#  Cloud-Based File Storage System 

---

##  Overview
This project simulates a simple **cloud-based file storage and retrieval system** using **pure Python**.  
Users can upload files, receive a **unique key**, and later **download** their files using that key — similar to a mini Google Drive, but command-line based.

This project was developed as part of the **Valise Technologies Internship** under Team Lead **Sindhu**.

---

##  Features
- 📂 **Upload any file** and store it safely in a local `storage/` folder  
- 🔑 **Generate a unique access key** for each uploaded file  
- 📜 **Maintain a dataset (`file_database.csv`)** to store file details  
- ⬇️ **Download files** anytime using the access key  
- 🧾 **View file list** and information directly from the terminal  

---

##  Folder Structure
Cloud_File_Storage/
├── main.py
├──downloads/
│   ├── filename.pdf
├── storage/
│   ├── <unique_key>_filename.pdf
├── file_database.csv
└── README.md

---

##  Technologies Used
| Component | Tool/Library |
|------------|---------------|
| Language | Python 3.10 |
| File Handling | `os`, `shutil` |
| Unique Key Generation | `uuid` |
| Dataset Storage | `csv` |
| Date & Time | `datetime` |

---

##  How to Run
1. Open your terminal and navigate to the project folder:
   ```bash
   cd ~/Cloud_File_Storage
2.	Run the main script:
   python3 main.py
3.	Choose one of the commands:
	•	upload → Upload a new file
	•	list → View all uploaded files
	•	download → Retrieve file using key
	•	info → Get file details by key
	•	exit → Quit the program
Example Usage:
>> upload
Enter the full path of file to upload: /Users/vizaa/Downloads/pan.pdf
✅ File uploaded successfully! Unique Key: 99bb6c31

>> list
Key | Original Filename | Stored Filename | Uploaded At
-------------------------------------------------------------
99bb6c31 | pan.pdf | 99bb6c31_pan.pdf | 2025-10-24 12:48:03

Dataset (file_database.csv)
key          original_filename        stored_filename        upload_timestamp
99bb6c31     pan.pdf                  99bb6c31_pan.pdf       2025-10-24 12:48:03


 Future Improvements
	•	Add authentication (user login & password)
	•	Add file expiry or sharing limits
	•	Integrate with cloud storage APIs (AWS S3, Google Drive)
	•	Add encryption for secure storage

 Conclusion

This project successfully demonstrates file handling, dataset creation, and key-based access using only Python.
It aligns with Valise Technologies’ learning goal: “Build efficient and simple solutions with clear logic and clean code.”






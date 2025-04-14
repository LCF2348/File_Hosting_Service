# File Hosting Service
**Steps to Start Working on the Project (Assuming You're on Windows 11):**

1. Choose a folder on your computer to place your project in, right click inside it and click "Open in Terminal".
   
2. Clone the repo and navigate into your new folder using the following commands in your terminal:
   ```bash
   git clone https://github.com/LCF2348/File_Hosting_Service.git
   cd File_Hosting_Service
**For the rest of the steps, continue execution in your terminal (after you've navigated into your project folder).**

3. Create a Virtual Environment to manage project dependencies:
   ```bash
   py -3 -m venv .venv
4. Activate the environment:
   ```
   .venv\Scripts\activate
5. Install Flask using pip:
   ```
   pip install Flask
6. Install SQLAlchemy using pip:
   ```
   pip install flask-sqlalchemy
Note that steps 3-6 are needed because our repo doesn't hold our virtual environment or Flask installation.

**Setting Up the Local Database to Talk to the Cloud:**
1. Navigate to the SQLite3 downloads page: https://www.sqlite.org/download.html
2. Underneath "Precompiled Binaries for Windows", download "sqlite-tools-win-x64-3490100.zip".
3. Extract the folder to your desired location (Documents, Desktop, etc.)
4. While still inside the folder, copy its location from the Windows Explorer address bar.
5. Press the Windows Key, and search for "Edit the system environment variables".
6. Clicking "Environment Variables", select the "Path" variable and click "Edit..."
7. Click "New", and paste the location of SQLite3 you exported earlier, and hit "OK".
8. In the project folder, open a terminal and entering the following commands, one at a time:
   ```
   flask shell
   db.create_all()
   exit()
9. Verify the database was created using the following commands, one at a time:
   ```
   sqlite3 instance/db.sqlite3
   .tables
   .schema
10. Run the project using "flask --app app run" in a terminal.
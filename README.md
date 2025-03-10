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
Note that steps 3-5 are needed because our repo doesn't hold our virtual environment or Flask installation.

**To Run the Project**
1. Navigate inside of the project folder, open a terminal and use the following command:
   ```bash
   flask --app hello run

2. Navigate to http://127.0.0.1:5000 in any web browser. Ctrl+C to quit.
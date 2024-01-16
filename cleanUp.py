#necessary modules
import os
import shutil
import schedule
import time
from datetime import datetime, timedelta

#function to perform cleanup
def cleanup_desktop():
    desktop_path = "C:\\Users\\chine\\Downloads"

    old_files_folder = os.path.join(desktop_path, "Old Files")
    today = datetime.now()

    if not os.path.exists(old_files_folder):
        os.makedirs(old_files_folder)

    #looping through each files in the downloads folder
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Check if it's a pdf file and older than 30 days
        if os.path.isfile(file_path)  and (filename.lower().endswith(".pdf")):
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            # and older than 30 days
            if (today - mod_time > timedelta(days=30)):
                # Move the file to the Old Files folder
                shutil.move(file_path, os.path.join(old_files_folder, filename))
                print(f"Moved {filename} to Old Files")

# Uncomment the line below to execute the cleanup
if __name__ == "__main__":
    # Schedule the task to run every 7 days
    schedule.every(7).days.at("12:00").do(cleanup_desktop)

    # Keep the script running to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)


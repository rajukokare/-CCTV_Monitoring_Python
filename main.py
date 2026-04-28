import os
import csv
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

# List of CCTV cameras (Replace with actual camera names and IP addresses)
cams = [
    {"name": "TEST_SHED_EXIT_SIDE_1", "ip": "192.168.1.15"},
    {"name": "TEST_SHED_BACK_SIDE", "ip": "192.168.1.16"},
    {"name": "VISUALS_CAM_3", "ip": "192.168.1.17"},
    {"name": "VISUALS_CAM_5", "ip": "192.168.1.18"},
    {"name": "VISUALS_CAM_2", "ip": "192.168.1.19"},
    {"name": "TEST_SHED_EXIT_SIDE_2", "ip": "192.168.1.20"},
    {"name": "TEST_SHED_EXIT_SIDE", "ip": "192.168.1.21"},
    {"name": "TEST_SHED_ENTRY_SIDE_1", "ip": "192.168.1.22"},
    {"name": "FRONT_OF_UTILITY_ROOM", "ip": "192.168.1.23"},
    {"name": "VISUALS_CAM_4", "ip": "192.168.1.24"},
    {"name": "VISUALS_CAM_1", "ip": "192.168.1.25"},
    {"name": "VISUALS_CAM_6", "ip": "192.168.1.26"},
    {"name": "DRIVERS_WAITING_AREA", "ip": "192.168.1.27"},
    {"name": "SERVER_ROOM", "ip": "192.168.1.28"},
    {"name": "ADMIN_POURCH", "ip": "192.168.1.29"},
    {"name": "PTZ_360", "ip": "192.168.1.30"},
    {"name": "ADMIN_AREA_OUTSIDE", "ip": "192.168.1.31"},
]
def send_alert(camera_name,camera_ip):
    msg=EmailMessage()
    msg.set_content(f"Alert! Your CCTV '{camera_name}' (ip:{camera_ip}) is offline, check immidiate..")
    msg['From'] = "kokare.raju@gmail.com"
    msg['To'] = "kokare.raju@gmail.com"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("kokare.raju@gmail.com", "yuwvlepdflqucdqr")
        server.send_message(msg)
        server.quit()
    except Exception as e :
        print (f"I am try to mail but I have some trouble to send you a mail:{e}")

def run_camera_check():
    file_name = "CCTV_Daily_Report_git.csv"
    file_exists = os.path.isfile(file_name)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"\n--- Checking Cameras at {now} ---")

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Add headers if the file is being created for the first time
        if not file_exists:
            writer.writerow(["Time", "Camera Name", "IP Address", "Status"])

        for c in cams:
            # Ping the camera IP address
            # -n 1 → send 1 packet
            # -w 1000 → wait for 1000 milliseconds (1 second)
            response = os.system(f"ping -n 1 -w 1000 {c['ip']} > nul")
            
            # Determine camera status based on ping response
            if response == 0:
                status = "ONLINE"
            else:
                status = "OFFLINE"
                send_alert(c['name'], c['ip']) # if camera is offline alert me.
            
            # Write the result to CSV file
            writer.writerow([now, c['name'], c['ip'], status])
            
            # Print status in console
            print(f"{c['name']} ({c['ip']}): {status}")

    print("--------------------------------------")
    print(f"CSV file updated successfully: {file_name}")

# Run the script continuously every 1 hour
while True:
    run_camera_check()
    print("Next check will run in 1 hour. Monitoring is active...")
    time.sleep(1 * 60 * 60)  # Sleep for 1 hour (in seconds)

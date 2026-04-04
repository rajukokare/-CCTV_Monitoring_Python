# CCTV_Uptime_Monitoring_Automation_Using Python
I have recently undertaken a project titled "CCTV Monitoring using Python," and I am striving to complete it soon.
<br>
I am owner of this project.
<br>
* 14 cameras had to be checked manually every three hours.
<br>
* Due to human error, the data was not consistently accurate.
<br>
* It was not possible to determine the exact time when a camera had stopped working.
<br>
# The solution is (What I do:)
<br>
* Automation: Automated the "ping" process using Python.
<br>
* Scheduling: Implemented a loop to run the script every 1 hour.
<br>
Logging(log_fine): The status (Online/Offline) of each camera is saved directly to a CSV file, making record-keeping easy.

# CCTV Uptime Monitoring Automation

## 📌 Problem Statement
In my current role, monitoring the status of 14 CCTV cameras was a manual and repetitive task. It had to be done every 3 hours, which was time-consuming and prone to human error.

## 🚀 Solution
I developed a Python automation script that:
* *Pings* each camera's IP address automatically.
* *Logs* the status (Online/Offline) with a timestamp.
* *Exports* the data into a CSV file for daily reporting.

## 🛠 Tech Stack
* *Language:* Python
* *Library:* os, csv, datetime
* *Output:* CSV (can be used for Excel Dashboards)

## 📊 Result
This automation reduced manual checking time by 100% and provided 100% accurate uptime data for management reports.

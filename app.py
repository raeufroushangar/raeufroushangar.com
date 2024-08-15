from flask import Flask, request, send_from_directory
import os
import csv
from datetime import datetime

app = Flask(__name__)

# Directory where your static site is located
SITE_ROOT = '/home/raeuf/projects/raeufroushangar.com/_site'

# Path to the log file
LOG_FILE = '/home/raeuf/projects/raeufroushangar.com/ip_logs.csv'

# Ensure the log file exists and has the correct headers
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['IP Address', 'Timestamp'])

@app.before_request
def log_ip():
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"IP {ip_address} accessed the site at {timestamp}")
    with open(LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ip_address, timestamp])


@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(SITE_ROOT, filename)

@app.route('/')
def serve_index():
    return send_from_directory(SITE_ROOT, 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

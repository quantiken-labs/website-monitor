import requests
import smtplib
import os
from time import sleep

# Configuration from environment variables
URL = os.getenv("MONITOR_URL", "https://example.com")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))  # seconds
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")

def send_email_alert():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        message = f"Subject: Website Down Alert!\n\n{URL} is down!"
        server.sendmail(EMAIL_USER, EMAIL_TO, message)
        server.quit()
        print(f"[ALERT] Email sent to {EMAIL_TO}")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

while True:
    try:
        response = requests.get(URL, timeout=10)
        if response.status_code != 200:
            print(f"[DOWN] Status code {response.status_code}")
            send_email_alert()
        else:
            print(f"[UP] Status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[DOWN] Exception: {e}")
        send_email_alert()
    sleep(CHECK_INTERVAL)

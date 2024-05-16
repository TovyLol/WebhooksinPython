import requests
import json

def send_webhook(webhook_url, message, author, title, color):
    payload = {
        "username": author,
        "embeds": [
            {
                "title": title,
                "description": message,
                "color": int(color[1:], 16)  # convert hex
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        response.raise_for_status() #exeption

        print("Webhook sent successfully!")
    except requests.exceptions.RequestException as e:
        print("Failed to send webhook:", e)

#strings
webhook_url = "your url"
message = "Webhook Creation successfull"
author = "Webhook school tester drenthe college"
title = "Dennis @ 2024"
color = "#FF5733"

send_webhook(webhook_url, message, author, title, color)
